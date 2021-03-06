#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 2
#SBATCH -t 0-02:00:00
#SBATCH -p parallel
#SBATCH -q normal
#SBATCH -o slurm.%j.out
#SBATCH -e slurm.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jgrassel@asu.edu
#SBATCH --export=video_in_dir='/scratch/jgrassel/video_in/',video_name='003_Scene_T21118_Trim.mp4',image_in_dir='/scratch/jgrassel/image_in3/'

module purge

module load python/3.7.1

python image_extraction.py