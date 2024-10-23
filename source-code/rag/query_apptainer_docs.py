#!/usr/bin/env python


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# Local apptainer documentation (.rst files)
documents = SimpleDirectoryReader("texts/").load_data()

# Embeddings model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Language model
Settings.llm = Ollama(model="llama3.2", request_timeout=360.0)

# Create index
index = VectorStoreIndex.from_documents(documents)

# Perform RAG query
query_engine = index.as_query_engine()

while True:
    query = input("Enter query: ")
    if query == "exit":
        break
    response = query_engine.query(query)
    print('\n' + response)
    print('\n' + '='*72 + '\n')
