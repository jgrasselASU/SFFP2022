import numpy as np
from saliency_metrics import video_salience_metrics as vsm

fixation_dir = 'old_reference/Fixations.txt'
sal_dir = 'gbvs_out/'

auc_score = vsm.range_auc_judd(245, 260, 'old_reference/Fixations.txt', 'gbvs_out/')

print(auc_score)