import os
import numpy as np

gbvs_results = np.load('gbvs_out/gbvs_results.npy')

print(gbvs_results.shape)

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
