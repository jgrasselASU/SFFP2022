#!/bin/bash

#SBATCH -N 1
#SBATCH -n 3
#SBATCH -c 1
#SBATCH -t 0-00:01:00
#SBATCH -p parallel
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu
#SBATCH --array 1-2
#SBATCH --export=export_var1='199',export_var2='299'

module purge

module load python/3.7.1

python test.py