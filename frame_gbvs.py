import os
import cv2
from saliency_models import gbvs
import json
import multiprocessing as mp
import time
from datetime import datetime
import numpy as np
from itertools import repeat


# Run GBVS code and adjust for numerical errors
def get_gbvs_data(img_num, save_dir):
    img = cv2.imread(image_in_dir + str(img_num) + '.jpg')
    sal_map = gbvs.compute_saliency(img)
    sal_map[np.where(sal_map < 0)] = 0
    sal_map[np.where(sal_map > 255)] = 255
    sal_map = sal_map.astype('uint8')
    np.save(save_dir + str(img_num) + '.npy', sal_map)
    # Saves .npy file that is a 2D matrix [row, column] same size as images
    return 1


# Check to see if this is running on the Agave cluster
# If so, use the scratch directory
if os.getenv('SLURM_CPUS_PER_TASK', 0) != 0:
    image_in_dir = str(os.getenv('image_in_dir'))
    gbvs_out_dir = str(os.getenv('gbvs_out_dir'))
    cpu_count = int(os.getenv('SLURM_CPUS_PER_TASK'))
else:  # Default for local testing
    image_in_dir = 'image_in/'
    gbvs_out_dir = 'gbvs_out/'
    cpu_count = 2 # Can adjust when running locally

# Load the video metadata json file
print('Retrieving metadata at ' + str(datetime.now()))
with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])
video_name = str(metadata['title'])

# Compute the GBVS saliency map for each frame in parallel
print('Starting Parallel computing: ' + str(datetime.now()))
start = time.perf_counter()
pool = mp.Pool(cpu_count)
pool.starmap(get_gbvs_data, zip([img_num for img_num in range(nb_frames)], repeat(gbvs_out_dir)))
pool.close()
end = time.perf_counter()
print('Finished parallel computing: ' + str(datetime.now()))
print('Parallel time to complete: ' + str(round(end-start, 2)))
