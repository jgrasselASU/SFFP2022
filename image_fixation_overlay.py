import numpy as np
from PIL import Image, ImageDraw
import json
import os

def get_heat_map(sal_map):
    heat = np.zeros((sal_map.shape[0], sal_map.shape[1], 4), dtype=np.uint8)

    ril = np.where(sal_map > 170)
    gil = np.where((sal_map > 85) & (sal_map <= 170))
    gdl = np.where(sal_map > 170)
    bil = np.where((sal_map > 0) & (sal_map <= 85))
    bdl = np.where((sal_map > 85) & (sal_map < 170))

    heat[ril[0], ril[1], 0] = (sal_map[ril]-170)*3
    heat[gil[0], gil[1], 1] = 255 - ((170 - sal_map[gil]) * 3)
    heat[gdl[0], gdl[1], 1] = 255 - ((sal_map[gdl] - 170) * 3)
    heat[bil[0], bil[1], 2] = 255 - ((85 - sal_map[bil]) * 3)
    heat[bdl[0], bdl[1], 2] = 255 - ((sal_map[bdl] - 85) * 3)

    heat[:, :, 3] = 210

    heat_img = Image.fromarray(heat, 'RGBA')
    return heat_img

# Check to see if this is running on the Agave cluster
# If so, use the scratch directory
if os.getenv('SLURM_CPUS_PER_TASK', 0) != 0:
    image_in_dir = str(os.getenv('image_in_dir'))
    gbvs_out_dir = str(os.getenv('gbvs_out_dir'))
    fixation_dir = str(os.getenv('fixation_dir'))
    cpu_count = int(os.getenv('SLURM_CPUS_PER_TASK'))
    eval_dir = 'evaluation_out/'
    overlay_dir = str(os.getenv('overlay_dir'))
else:  # Default for local testing
    image_in_dir = 'image_in/'
    gbvs_out_dir = 'gbvs_out/'
    fixation_dir = 'fixation_data/Fixations.txt'
    eval_dir = 'evaluation_out/'
    cpu_count = 3 # Can be adjusted when running locally


radius = 20
fixations = np.loadtxt(fixation_dir)

print('Loading metadata')
with open(image_in_dir + 'metadata.json') as json_file:
    metadata = json.load(json_file)

nb_frames = int(metadata['nb_frames'])
print('Number of frames: ' + str(nb_frames))

for i in range(nb_frames):
    print('Processing image: ' + str(i))
    img = Image.open(image_in_dir + str(i) + '.jpg')
    img = img.convert('RGBA')

    sal_map = np.load(gbvs_out_dir + str(i) + '.npy')
    heat_img = get_heat_map(sal_map)
    img = Image.alpha_composite(img, heat_img)

    if i in fixations[:, 0]:
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        frame_match = np.where(fixations[:, 0] == i)
        frame, x, y = fixations[frame_match][0]

        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(255, 255, 0, 150), outline=(0, 0, 0, 255))

        img = Image.alpha_composite(img, overlay)

    img = img.convert('RGB')
    img.save(overlay_dir + str(i) + '.jpg', quality=90)
