# Models

Directory intended to hold downloaded models. The directory contains scripts to
download the models rather than the models themselves as these are
prohibitively large to store in the repository.


## What is it?

1. `download-mistrallite.sh`: script to download the MISTRAL-Lite model (7B,
   Q4_K_M) from Hugging Face.
1. `Modelfile-mistrallite.Q4_K_M`: model file for MISTRAL-Lite for using it in
   ollama.
1. `download-llama-3.2-3B.sh`: script to download the LLAMA 3.2 model (3B) from
   Hugging Face. (**Note**: this is a gated model, so you need to request
   access to it.  Consequently, it requires a Hugging Face access token and
   logging in to download.)
