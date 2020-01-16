#!/usr/bin/env python
# vim:fileencoding=utf-8
import os
from tqdm import trange

os.chdir('..')
os.chdir('./testIndex.crpsp')
print('CWD Done!')

os.system("touch log.txt")

for i in trange(100):
    i_id = f"{i:02d}"  # name of the folder (adds a 0 to 01)
    for j in trange(100):
        j_id = f"{j:02d}"  # name of the folder (adds a 0 to 01)
        for k in trange(100):
            k_id = f"{k:02d}"  # name of the folder (adds a 0 to 01)
            log_action = "X : "+str(i_id)+"-"+str(j_id)+"-"+str(k_id)+".xml\n"
            log_file = open("./log.txt",'a')
            log_file.write(log_action)
            log_file.close()

