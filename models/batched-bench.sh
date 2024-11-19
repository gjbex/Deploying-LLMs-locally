#!/usr/bin/env bash

llama-batched-bench -m "$1" \
    --ctx-size 2048 \
    --batch-size 2048 \
    --ubatch-size 512 \
    -npp 128,256,512 -ntg 128,256 \
    -npl 1,2,4,8,16,32
