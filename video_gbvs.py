import cv2
import numpy as np
from saliency_models import gbvs

vidcap = cv2.VideoCapture('video_in/drive1.mp4')
success, image = vidcap.read()
size = (image.shape[1], image.shape[0])
count = 0

vid_out = cv2.VideoWriter('video_out/sal_video1.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 29.97, size)

while success:
    print('Processing Frame', count)
    frame_sal_map = gbvs.compute_saliency(image)
    cv2.imwrite("video_out/frame_im%d.jpg" % count, image)
    cv2.imwrite("video_out/frame_sal%d.jpg" % count, frame_sal_map)

    frame_sal_map = cv2.cvtColor(frame_sal_map, cv2.COLOR_GRAY2RGB)

    frame_sal_map = np.uint8(frame_sal_map)

    vid_out.write(frame_sal_map)

    success, image = vidcap.read()
    print('Read a new frame: ', success)

    count += 1

vid_out.release()