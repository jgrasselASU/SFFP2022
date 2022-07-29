#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 2
#SBATCH -t 0-04:00:00
#SBATCH -p parallel
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu
#SBATCH --export=image_in_dir='/scratch/jgrassel/image_in1/',gbvs_out_dir='/scratch/jgrassel/gbvs_out1/',fixation_dir='/home/jgrassel/SFFP2022/fixation_data/fixation1.txt',overlay_dir='/home/jgrassel/SFFP2022/image_fixation_overlay1/'

module purge

module load python/3.7.1

python image_fixation_overlay.py