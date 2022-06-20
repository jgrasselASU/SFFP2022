import json
import cv2
import ffmpeg
from datetime import datetime
import os

# Runs in about double the time of the length of the video
# Check whether on cluster or not
if os.getenv('image_in_dir', 0) != 0:
    image_in_dir = str(os.getenv('image_in_dir'))
    video_name = str(os.getenv('video_name'))
    video_in_dir = str(os.getenv('video_in_dir'))
else:  # Default for local testing
    video_in_dir = 'video_in/'
    video_name = 'drive1.mp4'
    image_in_dir = 'image_in/'

# Get metadata for frame size and frame rate for later use
print("Getting metadata: " + str(datetime.now()))
metadata = ffmpeg.probe(video_in_dir + video_name)
metadata = metadata['streams'][0]       # ['width', 'height', 'r_frame_rate', 'nb_frames']
metadata['title'] = video_name
json_meta = json.dumps(metadata, indent=4)
f = open(image_in_dir + 'metadata.json', 'w')
f.write(json_meta)
f.close()
print("Metadata writing complete: " + str(datetime.now()))

# Read the video and write each image individually
print("Processing video: " + str(datetime.now()))
vidcap = cv2.VideoCapture(video_in_dir + video_name)
success, image = vidcap.read()
count = 0
while success:
    print('Processing Frame', count)
    cv2.imwrite(image_in_dir + "%d.jpg" % count, image)
    success, image = vidcap.read()
    count += 1
print("Finished processing video: " + str(datetime.now()))
