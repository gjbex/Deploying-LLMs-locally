'''Recipe to create either a Docker container or Singularity image
for a container to run Ollama tools.

Usage:
    $ hpccm  --recipe ollama.py  --format docker
    $ hpccm  --recipe ollama.py  --format singularity
'''

# Choose a base image
Stage0.baseimage('ghcr.io/ggerganov/llama.cpp:full-cuda')
 
# Install helper software
Stage0 += apt_get(ospackages=['wget', 'unzip', 'git',])

# Add /app directory to PATH
Stage0 += environment(variables={'PATH': '/app:/bin:$PATH'})

# add run script, i.e., start bash
Stage0 += runscript(commands=['llama-cli'])
