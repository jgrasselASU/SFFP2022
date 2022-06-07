#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH -t 0-00:60:00
#SBATCH -p serial
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu
#SBATCH --array 1-2
#SBATCH --export=export_var='299'

module purge

module load python/3.7.1

python test.py