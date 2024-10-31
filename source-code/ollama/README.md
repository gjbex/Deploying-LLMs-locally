# Ollama

Ollama is a tool to manage machine learning (AI) models.  It can
be used to download and run models.


## What is it?

1. `Modelfile-marvin`: a file that describes the "marvin" model
   based on a pre-trained model.  It sets the temperature of the model
   and provides a system prompt to make the model act like Marvin, the
   paranoid android from the Hitchhiker's Guide to the Galaxy.
1. `images`: a directory containing images that can be used to test
   interact with multimodal models.


## How to use it?

If not already done, start the ollama server:
```bash
$ ollama serve
```

To create the initial model:
```bash
$ ollama create marvin -f Modelfile-marvin
```

To run the model:
```bash
$ ollama run marvin
```
