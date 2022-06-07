import os

i = int(os.environ["SLURM_ARRAY_TASK_ID"])
j = int(os.environ["export_var1"])
k = int(os.environ["export_var2"])

print('My task id: ' + str(i))
print('My Export Var: ' + str(j))
print(os.environ)
