#!/usr/bin/env bash

# Download the MISTRAL-Lite model
huggingface-cli download  TheBloke/MistralLite-7B-GGUF  \
    mistrallite.Q4_K_M.gguf \
    --local-dir .           \
    --local-dir-use-symlinks False
