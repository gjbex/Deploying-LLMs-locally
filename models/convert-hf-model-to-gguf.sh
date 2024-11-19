#!/usr/bin/env bash

apptainer exec --nv llama.cpp.sif /bin/python3 /app/convert_hf_to_gguf.py "$@"
