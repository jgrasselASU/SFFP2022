import numpy as np
from PIL import Image, ImageDraw
import json
import os

def get_heat_map(sal_map):
    heat = np.zeros((sal_map.shape[0], sal_map.shape[1], 4), dtype=np.uint8)
    heat[:, :, 0] = ((sal_map^2)/255) * 0.8
    heat[:, :, 1] = sal_map
    heat[:, :, 2] = 255-sal_map
    heat[:, :, 3] = 200-(sal_map * 0.5)
    heat_img = Image.fromarray(heat, 'RGBA')
    return heat_img

radius = 20
fixations = np.loadtxt('old_reference/Fixations.txt')

image_in_dir = 'image_in/'
gbvs_out_dir = 'gbvs_out/'
cpu_count = 4

print('Loading metadata')
with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])
print('Number of frames: ' + str(nb_frames))

for i in range(nb_frames):
    print('Processing image: ' + str(i))
    img = Image.open('image_in/' + str(i) + '.jpg')
    img = img.convert('RGBA')

    sal_map = np.load(gbvs_out_dir + str(i) + '.npy')
    heat_img = get_heat_map(sal_map)
    img = Image.alpha_composite(img, heat_img)

    if i in fixations[:, 0]:
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        frame_match = np.where(fixations[:, 0] == i)
        frame, x, y = fixations[frame_match][0]

        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(255, 0, 0, 80), outline=(0, 0, 0, 255))

        img = Image.alpha_composite(img, overlay)

    img = img.convert('RGB')
    img.save('image_fixation_overlay/' + str(i) + '.jpg', quality=95)
