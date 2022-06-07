import os

i = int(os.environ["SLURM_ARRAY_TASK_ID"])
j = int(os.environ["export_var"])

print('My task id: ' + str(i))
print('My Export Var: ' + str(j))
print('My CPU Count: ' + str(os.cpu_count()))
