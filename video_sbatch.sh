#!/bin/bash

#SBATCH -N 1
#SBATCH -n 28
#SBATCH -t 0-00:10:00
#SBATCH -p serial
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=%u@asu.edu
#SBATCH --export=NONE

module purge

module load python/3.7.1

python video_gbvs.py