# Tools

This directory contains tools that are used for this training.


## What is it?

1. `ollama.py`: an hpccm script to generate a Dockerfile or Singularity
   definition file for running the Ollama application.
1. `ollama.recipe`: a Singularity recipe for building an image to run
   Ollama.
1. `llama.cpp.py`: an hpccm script to generate a Dockerfile or Singularity
   definition file for building the llama.cpp application.
1. `llama.cpp.recipe`: a Singularity recipe for building an image to build
   an image to run llama.cpp.
1. `apptainer_build.slurm`: a Slurm script to build an Apptainer image.
   (Note: you may have to adapt this script to your environment.)
