#!/usr/bin/env python3.7

import os
import glob

path = os.getcwd()
files = []
for file in glob.glob(path + '/*'):
    files.append({"path":file, "size":os.path.getsize(file)})
    
for i in range(len(files)):
    print(files[i])

    
