import numpy as np
from saliency_metrics import video_salience_metrics as vsm
import os
from datetime import datetime
import json
import multiprocessing as mp
from itertools import repeat

# Check to see if this is running on the Agave cluster
# If so, use the scratch directory
if os.getenv('SLURM_CPUS_PER_TASK', 0) != 0:
    image_in_dir = str(os.getenv('image_in_dir'))
    gbvs_out_dir = str(os.getenv('gbvs_out_dir'))
    fixation_dir = str(os.getenv('fixation_dir'))
    cpu_count = int(os.getenv('SLURM_CPUS_PER_TASK'))
    eval_dir = 'evaluation_out/'
else:  # Default for local testing
    image_in_dir = 'image_in/'
    gbvs_out_dir = 'gbvs_out/'
    fixation_dir = 'fixation_data/Fixations.txt'
    eval_dir = 'evaluation_out/'
    cpu_count = 3 # Can be adjusted when running locally

# Load the video metadata json file
print('Retrieving metadata at ' + str(datetime.now()))
with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])
video_name = str(metadata['title'])

# ------ Evaluation Parameters ----- #
rad = 5  # Frame radius forward and backward analyzed for each data point
# E.g. rad = 5, then when determining the metric for frame 7, frames 2 through 12 will be analyzed
frame_sigma = 6  # Gaussian blur through time standard deviation
px_sigma = 45  # Gaussian blur spatially

# ------------- Evaluate Video Using Rolling AUC ---------------- #
print('Starting AUC evalutation')
pool = mp.Pool(cpu_count)
auc_judd_results = pool.starmap(vsm.range_auc_judd,
                           zip([s for s in range(0, nb_frames-rad)],
                               [e for e in range(rad, nb_frames)],
                               repeat(fixation_dir),
                               repeat(gbvs_out_dir)))
pool.close()
np.savetxt(eval_dir + 'auc_judd_' + video_name + '_rad' + str(rad) + '.txt', auc_judd_results)
print('AUC evaluation complete')

# ------------- Evaluate Video Using Rolling Pearson's Correlations ---------------- #
print("Starting Pearson's correlation evaluation")
pool = mp.Pool(cpu_count)
cc_results = pool.starmap(vsm.range_cc,
                           zip([s for s in range(0, nb_frames-rad)],
                               [e for e in range(rad, nb_frames)],
                               repeat(fixation_dir),
                               repeat(gbvs_out_dir),
                               repeat(frame_sigma),
                               repeat(px_sigma)))
pool.close()
np.savetxt(eval_dir + 'cc_' + video_name + '_rad' + str(rad) + '_fs' + str(frame_sigma) + '_pxs' + str(px_sigma), cc_results)
print('Correlation evaluation complete')
