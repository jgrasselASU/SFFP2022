import cv2
import os
from saliency_models import gbvs
import json
import multiprocessing as mp
import time
from datetime import datetime


def get_gbvs_data(img_num):
    print('Computing image: ' + str(img_num) + ' at ' + str(datetime.now()))
    img = cv2.imread(image_in_dir + str(img_num) + '.jpg')
    sal_map = gbvs.compute_saliency(img)
    return sal_map


image_in_dir = str(os.environ['image_in_dir'])
cpu_count = int(os.environ['SLURM_CPUS_PER_TASK'])

# image_in_dir = 'image_in'
# cpu_count = 2

with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])

# parallel
start = time.perf_counter()
pool = mp.Pool(cpu_count)
results = pool.map(get_gbvs_data, [img_num for img_num in range(nb_frames)])
pool.close()
end = time.perf_counter()
print('Parallel time to complete: ' + str(round(end-start, 2)))

# #single
# start = time.perf_counter()
# results = []
# for img_num in range(nb_frames):
#     results.append(get_gbvs_data(img_num))
# end = time.perf_counter()
# print(results)
# print('Single Thread: '+ str(round(end-start, 2)))
