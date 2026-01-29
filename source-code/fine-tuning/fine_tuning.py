#!/usr/bin/env python

from datetime import datetime
import os
import sys
from accelerate import Accelerator
from dotenv import load_dotenv
from datasets import load_dataset
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model
import torch
import transformers
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)


def format_prompt(example):
    return f'### Question: {example["input"]}\n### Answer: {example["output"]}'

def generate_and_tokenize_prompt(prompt):
    return tokenizer(
        format_prompt(prompt),
        max_length=200,
        padding="max_length"
    )

def print_trainable_parameters(model):
    """
    Prints the number of trainable parameters in the model.
    """
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param:.2f}"
    )

# os.environ['BNB_CUDA_VERSION'] = '120'
load_dotenv()

train_dataset = load_dataset(
    'json',
    data_files='pandas_data_analysis_questions_train.jsonl',
    split='train'
)
test_dataset = load_dataset(
    'json',
    data_files='pandas_data_analysis_questions_test.jsonl',
    split='train'
)

base_model_id = "mistralai/Mistral-7B-v0.1"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(
    base_model_id,
    padding_side="left",
    add_eos_token=True,
    add_bos_token=True,
)
tokenizer.pad_token = tokenizer.eos_token

tokenized_train_dataset = train_dataset.map(generate_and_tokenize_prompt)
tokenized_test_dataset = test_dataset.map(generate_and_tokenize_prompt)


evaluation_prompt = "How to concatenate two dataframes along rows?"

evaluation_tokenizer = AutoTokenizer.from_pretrained(
    base_model_id,
    add_bos_token=True,
)

model_input = evaluation_tokenizer(
    evaluation_prompt,
    return_tensors="pt"
).to("cuda")

model.eval()
with torch.no_grad():
    print(evaluation_tokenizer.decode(
              model.generate(
                  **model_input,
                  max_new_tokens=256,
                  repetition_penalty=1.15)[0],
        skip_special_tokens=True))


print(model)

model.gradient_checkpointing_enable()
kbit_training_model = prepare_model_for_kbit_training(model)

config = LoraConfig(
    r=32,
    lora_alpha=64,
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
        "lm_head",
    ],
    bias="none",
    lora_dropout=0.05,  # Conventional
    task_type="CAUSAL_LM",
)

peft_model = get_peft_model(kbit_training_model, config)
print_trainable_parameters(peft_model)
print(peft_model)


# In[29]:




# In[30]:


if torch.cuda.device_count() > 1: # If more than 1 GPU
    peft_model.is_parallelizable = True
    peft_model.model_parallel = True

accelerator = Accelerator()
accelerated_model = accelerator.prepare_model(peft_model)

project = 'pandas_questions'
base_model_name = "mistral"
run_name = f'{base_model_name}-{project}'
output_dir = f'./{run_name}'
learning_rate = 2.5e-5

trainer = transformers.Trainer(
    model=accelerated_model,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_test_dataset,
    args=transformers.TrainingArguments(
        output_dir=output_dir,
        warmup_steps=2,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=1,
        gradient_checkpointing=True,
        max_steps=500,
        learning_rate=learning_rate,
        bf16=True,
        optim="paged_adamw_8bit",
        logging_steps=25,              # When to start reporting loss
        logging_dir="./logs",        # Directory for storing logs
        save_strategy="steps",       # Save the model checkpoint every logging step
        save_steps=25,                # Save checkpoints every 50 steps
#        evaluation_strategy="steps", # Evaluate the model every logging step
        eval_steps=25,               # Evaluate and save checkpoints every 50 steps
        do_eval=True,                # Perform evaluation at the end of training
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

accelerated_model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
trainer.train()
