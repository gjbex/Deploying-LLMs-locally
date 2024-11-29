#!/usr/bin/env -S bash -l
#SBATCH --account=lp_gpgpu_training
#SBATCH --nodes=1  --ntasks=1  --gpus-per-node=1
#SBATCH --time=00:30:00
#SBATCH --cluster=genius  --partition=gpu_p100

# Check whether the environment file name has been passed
# either as an environment variable or via the
# --export=ALL,ENVIRONMENT_FILE=... sbatch option.
# If not, terminate
if [ -z $ENVIRONMENT_FILE ]
then
    (>&2 echo "ENVIRONMENT_FILE not set")
    exit 1
fi

# Extract the environment name for the environment file
ENVIRONMENT_NAME=$(tail -n 1 $ENVIRONMENT_FILE | awk -F'/' '{print $NF}')

# Initialize conda/mamba
if [ -f ./mamba_init.sh ]
then
    source ./mamba_init.sh
elif [ -f ~/mamba_init.sh ]
then
    source ~/mamba_init.sh
elif [ -f ~/.mamba_init.sh ]
then
    source ~/.mamba_init.sh
else
    (>&2 echo "mamba is not initialized, environment creation may fail" )
fi

mamba env create -n $ENVIRONMENT_NAME -f $ENVIRONMENT_FILE
