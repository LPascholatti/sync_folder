import os

#Source path here:
source_dir = "./source"

#Assert that source is a directory:
assert os.path.isdir(source_dir), f"{source_dir} is not a directory"

files_source = os.listdir(source_dir)

for file in files_source:
    print(file)