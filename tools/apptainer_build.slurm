#!/usr/bin/env -S bash -l
#SBATCH --account=lp_gpgpu_training
#SBATCH --nodes=1  --ntasks=1  --gpus-per-node=1
#SBATCH --time=00:30:00
#SBATCH --cluster=genius  --partition=gpu_p100

if [ -z $RECIPE ]
then
    (>&2 echo "RECIPE not set")
    exit 1
fi

IMAGE=$(basename "${RECIPE%.*}.sif")

export APPTAINER_TMPDIR=$VSC_SCRATCH/singularity_tmp
mkdir -p $APPTAINER_TMPDIR
export APPTAINER_CACHEDIR=$VSC_SCRATCH/singularity_cache
mkdir -p $APPTAINER_CACHEDIR

apptainer build --force --fakeroot $IMAGE $RECIPE
