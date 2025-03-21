'''Recipe to create either a Docker container or Singularity image
for a container to run Ollama tools.

Usage:
    $ hpccm  --recipe ollama.py  --format docker
    $ hpccm  --recipe ollama.py  --format singularity
'''

# Choose a base image
Stage0.baseimage('ollama/ollama:latest')
 
# add run script, i.e., start ollama
Stage0 += runscript(commands=['ollama'])
