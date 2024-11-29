# OpenAI API

OpenAI provides an API to interact with its models.  This directory illustrates
how to use the OpenAI API to interact with ChatGPT.


## What is it?

1. `environment.yml`: conda environment file for installing the necessary
   dependencies.
1. `openai-api.ipynb`: illustrates how to use the OpenAI API to interact with
   ChatGPT.


## Important note

The OpenAI API requires an API key, which is not included in this repository.
If you want to access OpenAI models beyond ChatGPT 3.5, you will need
to obtain an API key from OpenAI.  Additionally, you will need credits to use
the API.  This is *not* free.

Concretely, you can set the API key in a `.env` file, and use the `python-dotenv`
module to load it into the environment.
```bash
OPENAI_API_KEY=your_api_key
```

Do **not** commit the `.env` file to the repository or share it in any other way.
