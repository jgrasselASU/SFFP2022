#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 2
#SBATCH -t 0-01:00:00
#SBATCH -p parallel
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu
#SBATCH --export=video_in_dir='/scratch/jgrassel/video_in/',video_name='riese_drive_5min.mp4',image_in_dir='/scratch/jgrassel/image_in/'

module purge

module load python/3.7.1

python image_extraction.py