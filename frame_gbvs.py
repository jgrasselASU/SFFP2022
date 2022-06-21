import os
import cv2
from saliency_models import gbvs
import json
import multiprocessing as mp
import time
from datetime import datetime
import numpy as np


def get_gbvs_data(img_num):
    print('Computing image: ' + str(img_num) + ' at ' + str(datetime.now()))
    img = cv2.imread(image_in_dir + str(img_num) + '.jpg')
    sal_map = gbvs.compute_saliency(img)
    sal_map[np.where(sal_map < 0)] = 0
    sal_map[np.where(sal_map > 255)] = 255
    return np.array(sal_map)


# Check whether on cluster or not
if os.getenv('image_in_dir', 0) != 0:
    image_in_dir = str(os.getenv('image_in_dir'))
    gbvs_out_dir = str(os.getenv('gbvs_out_dir'))
    cpu_count = int(os.getenv('SLURM_CPUS_PER_TASK'))
else:  # Default for local testing
    image_in_dir = 'image_in/'
    gbvs_out_dir = 'gbvs_out/'
    cpu_count = 4

# --- Video Input Metadata --- #
print('Retrieving metadata at ' + str(datetime.now()))
with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])
video_name = str(metadata['title'])

# --- Parallel GBVS Computation ---#
print('Starting Parallel computing: ' + str(datetime.now()))
start = time.perf_counter()
pool = mp.Pool(cpu_count)
results = pool.map(get_gbvs_data, [img_num for img_num in range(nb_frames)])
pool.close()
end = time.perf_counter()
results = np.array(results)
print('Finished parallel computing: ' + str(datetime.now()))
print('Parallel time to complete: ' + str(round(end-start, 2)))

print('Saving numpy array: ' + str(datetime.now()))
np.save(gbvs_out_dir + video_name + '.npy', results)  # gbvs_results[frame,row,column]

print('frame_gbvs complete at: ' + str(datetime.now()))

# #single (outdated, refer to parallel)
# print('Starting Single computing: ' + str(datetime.now()))
# start = time.perf_counter()
# results = []
# for img_num in range(nb_frames+1):
#     gbvs_mat = get_gbvs_data(img_num)
#     results = np.stack((results, gbvs_mat))
#     np.savetxt('gbvs_out.txt', gbvs_mat)
#     print(gbvs_mat.shape)
# end = time.perf_counter()
# print('Finishing single computing: ' + str(datetime.now()))
# print('Single Thread: '+ str(round(end-start, 2)))
