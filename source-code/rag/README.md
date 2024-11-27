# Retrieval-Augmented Generation (RAG)

Here you find examples for Retrieval-Augmented Generation (RAG) using
llamma-index.


## What is it?

1. `environment.yml`: a conda environment file that specifies the dependencies
   for the examples.
1. `texts`: a directory containing text files that can be used as documents for
   retrieval.  The text files are in `.rst` format, and are the [documentation
   of Apptainer](https://apptainer.readthedocs.io/en/latest/).
1. `query_apptainer_docs.py`: a Python script that uses the `llama_index`
   package to index the text files in the `texts` directory, and then uses the
   index to generate answers to questions.  It uses `BAAI/bge-base-en-v1.5`
   (Hugging Face) to create an embeeding and llama3.2 as the Large Language
   Model (LLM).
