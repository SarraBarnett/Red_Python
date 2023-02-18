#!/usr/bin/env python3.7

# importing os module 
import os

# importing glob module 
import glob

# defining the current working directory as "cwd" variable
cwd = os.getcwd()

# making an empty list named "cwd_files"
cwd_files = []

# using a "for" loop with glob function to retrieve all files/pathnames
# from the cwd 
for file in glob.glob(cwd + '/*'):
    
    # creating a dictionary "cwd_files_dict" that stores the path and size of each file
    cwd_files_dict = {"path":file, "size":os.path.getsize(file)}
    
    # append the dictionary to the cwd_files list
    cwd_files.append(cwd_files_dict)
 
# using a "for" loop with range() function to print the files pretty 
for i in range(len(cwd_files)):
    print(cwd_files[i])