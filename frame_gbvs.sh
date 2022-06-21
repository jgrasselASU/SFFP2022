#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 28
#SBATCH -t 0-12:00:00
#SBATCH -p parallel
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu
#SBATCH --export=image_in_dir='/scratch/jgrassel/image_in/',gbvs_out_dir='/scratch/jgrassel/gbvs_out/'

module purge

module load python/3.7.1

python frame_gbvs.py