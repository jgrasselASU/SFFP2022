import os
import numpy as np
import scipy.io
import ffmpeg
import json

sal_map = np.load('gbvs_out/drive1.mp4.npy')

# for i in range(sal_map.shape[0]):
#     for j in range(sal_map.shape[1]):
#         for k in range(sal_map.shape[2]):
#             if sal_map[i,j,k] > 255:
#                 sal_map[i,j,k] = 255
#             elif sal_map[i,j,k] < 0:
#                 sal_map[i,j,k] = 0

print(np.sum(sal_map < 0))
print(np.sum(sal_map > 255))
print(np.sum(sal_map))

sal_map[np.where(sal_map < 0)] = 0
sal_map[np.where(sal_map > 255)] = 255

print(np.sum(sal_map < 0))
print(np.sum(sal_map > 255))
print(np.sum(sal_map))

# m = scipy.io.loadmat('old_reference/freeNorm er0043startingatsecondtrial 2012-06-01 003.mat')
#
# print(m['eyetrackRecord']['x'])
# print(m['eyetrackRecord']['y'])
# print(m['eyetrackRecord']['pa'])
# print(m['eyetrackRecord']['t'])

# metadata = ffmpeg.probe('video_in/drive1.mp4')
# metadata['streams'][0]['vid_title'] = 'drive1.mp4'
# metadata = json.dumps(metadata['streams'][0]['title'], indent=4)
# print(metadata)
# metadata = metadata['streams'][0]       # ['width', 'height', 'r_frame_rate', 'nb_frames']
# json_meta = json.dumps(metadata, indent=4)
# f = open(image_in_dir + 'metadata.json', 'w')
# f.write(json_meta)
# f.close()

# i = int(os.environ['SLURM_ARRAY_TASK_ID'])
# j = int(os.environ['SLURM_ARRAY_TASK_COUNT'])
#
# n = int(os.environ['SLURM_NTASKS'])
#
# k = int(os.environ['export_var1'])
# l = int(os.environ['export_var2'])
#
# c = int(os.environ['SLURM_CPUS_PER_TASK'])
#
# print('My array task id: ' + str(i))
# print('Total array task count: ' + str(j))
# print('Total number of tasks: ' + str(n))
# print('My Export Var1: ' + str(k))
# print('My Export Var2: ' + str(l))
