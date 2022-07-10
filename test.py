import PIL.Image
import numpy as np
from PIL import Image, ImageDraw
import json
import os
import scipy.io
from scipy.ndimage import gaussian_filter
from saliency_metrics import video_salience_metrics as vsm
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
# from matplotlib.pyplot import figure

# --------- Creating an Image Overlay Dashboard --------------- #

auc_judd = np.loadtxt('evaluation_out/auc_judd_riese_drive_30sec.mp4_rad5')

fig = plt.figure(figsize=(10, 2), dpi=100)
plt.plot(auc_judd)

fig.savefig('test_img_plt', dpi=100)

img = PIL.Image.frombytes('RGB', fig.get_width_height(), fig.tostring_rgb())

img.save('test_img_pil.jpg')



# fixations = np.loadtxt('old_reference/Fixations.txt')
#
# sal_map = []
# gt = []
#
# for i in range(172, 192):
#     tmp_sal = np.load('gbvs_out/' + str(i) + '.npy')
#     sal_map.append(tmp_sal)
#
#     tmp_gt = np.zeros(tmp_sal.shape)
#
#     if i in fixations[:, 0]:
#         frame_match = np.where(fixations[:, 0] == i)
#         frame, col, row = fixations[frame_match][0]
#         tmp_gt[int(np.round(row)), int(np.round(col))] = 1
#
#     gt.append(tmp_gt)
#
#
# sal_map = np.stack(sal_map, axis=0)
# sal_map = vsm.normalize_map(sal_map)
#
# gt = np.stack(gt, axis=0)
# gt_cont = gt*1000
# gt_cont = gaussian_filter(gt_cont, sigma=[5, 45, 45])
# gt_cont = vsm.normalize_map(gt_cont)
#
# cc_score = vsm.cc(sal_map, gt_cont)
# auc_score = vsm.v_auc_judd(sal_map, gt)
#
# print(cc_score)
# print(auc_score)
#
# v_auc = vsm.v_auc_judd(sal_map, gt)
#
# print(v_auc)

# ---------------------- OLD CODE -------------------------- #

# m = scipy.io.loadmat('old_reference/freeNorm er0043startingatsecondtrial 2012-06-01 003.mat')
#
# x = m['eyetrackRecord']['x'][0][0][0]
# y = m['eyetrackRecord']['y'][0][0][0]
# t = m['eyetrackRecord']['t'][0][0][0]
# missing = m['eyetrackRecord']['missing'][0][0][0]
#
# for i in range(x.shape[0]):
#     print(x[i])
#     print(y[i])
#     print(t[i])
#     print(missing[i])

# sal_map = np.load('gbvs_out/0.npy')
#
# heat = np.zeros((sal_map.shape[0],sal_map.shape[1], 4), dtype=np.uint8)
#
# print(sal_map)
#
# def get_heat_map(sal_map):
#     heat[:, :, 3] = (255-sal_map) * 0.8
#     heat[:, :, 0] = sal_map
#     heat[:, :, 1] = sal_map
#     heat[:, :, 2] = sal_map
#     heat_img = Image.fromarray(heat, 'RGBA')
#     return heat_img
#
# print(heat)
#
# heat_img = Image.fromarray(heat, 'RGBA')
#
# img = Image.open('image_in/0.jpg')
# img = img.convert('RGBA')
#
# out_img = Image.alpha_composite(img, heat_img)
#
# out_img = out_img.convert('RGB')
#
# out_img.save('old_reference/heatmap_test.jpg', quality=95)
####################################################################
# fixations = np.loadtxt('old_reference/Fixations.txt')
#
# print(15 in fixations[:, 0])
#
# frame_match = np.where(fixations[:, 0] == 0)
# frame, x, y = fixations[frame_match][0]
#
# print(x)
# print(y)

# m = scipy.io.loadmat('old_reference/freeNorm er0043startingatsecondtrial 2012-06-01 003.mat')
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
