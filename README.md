# Deploying LLMs locally

This is a repository that illustrates the use of various AI tools and
techniques and how to use them on local infrastructure such as HPC systems.


## What is it?

1. `local_LLMs.pptx`: PowerPoint presentation on running Large Language
   Models (LLMs) on a local machine.
1. `source-code`: directory with the source code.
1. `models`: directory with scripts to download pre-trained models.
1. `data`: directory with scripts to download data.
1. `tools`: directory with tools to run LLMs on a local machine.
1. `docs`: directory for a web site on this training.
1. `CONTRIBUTING.md`: guidelines for contributing to this repository.
1. `LICENSE`: license information for this repository.
1. `CODE_OF_CONDUCT.md`: code of conduct for this repository and training.


## Conda environments

Since conda environments for machine learning have many dependencies, we
opted to have a separate environment for each directory in `source-code`,
rather than one environment for all code.  This makes it easier to manage
dependencies, and to avoid conflicts between different packages that may
be required by different scripts.
