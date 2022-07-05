import numpy as np
from saliency_metrics import video_salience_metrics as vsm
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import os
from datetime import datetime
import json

# Check whether on cluster or not
if os.getenv('SLURM_CPUS_PER_TASK', 0) != 0:
    image_in_dir = str(os.getenv('image_in_dir'))
    gbvs_out_dir = str(os.getenv('gbvs_out_dir'))
    cpu_count = int(os.getenv('SLURM_CPUS_PER_TASK'))
else:  # Default for local testing
    image_in_dir = 'image_in/'
    gbvs_out_dir = 'gbvs_out/'
    cpu_count = 2

# --- Video Input Metadata --- #
print('Retrieving metadata at ' + str(datetime.now()))
with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])
video_name = str(metadata['title'])
#------------------------------#

fixation_dir = 'old_reference/Fixations.txt'

rad = 5

auc_results = []

for i in range(rad, nb_frames-rad):
    print('Processing range: ' + str(i-rad) + ', ' + str(i+rad))
    auc_score = vsm.range_auc_judd(i-rad, i+rad, 'old_reference/Fixations.txt', gbvs_out_dir)
    auc_results.append(auc_score)

figure(figsize=(10, 2), dpi=100)

plt.plot(auc_results)
plt.savefig('auc_results')
