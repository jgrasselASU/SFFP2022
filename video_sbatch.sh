#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH -array 1-3
#SBATCH -t 0-00:60:00
#SBATCH -p parallel
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu

module purge

module load python/3.7.1

python video_gbvs.py