import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
print("Hello")
print(hdir)
# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

print(pattern)
# TODO: Use the glob.glob() function to obtain the list of filenames
# file_name_false = glob.glob(pattern, recursive=False)
# print(file_name_false)
#
# file_name_true = glob.glob(pattern, recursive=True)
# print(file_name_true)

file_name = glob.glob(pattern)
print(file_name)
# UNSURE ABOUT RECURSIVE
# TODO: use os.path.getsize to find each file's size
file_size_dict = {}

for file in file_name:
    file_size = os.path.getsize(file)
    file_size_dict[file] = file_size
print(file_size_dict)
# TODO: Add a test to only display files that are not zero length
for file in file_name:
    if file_size_dict[file] != 0:
        print(file)
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
for file in file_name:
    print(os.path.basename(file))
