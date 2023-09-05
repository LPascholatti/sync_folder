import os
import shutil

# Source and replica paths here:
source_dir = "./source"
replica_dir = "./replica"

# Assert that source and replica are a directory:
assert os.path.isdir(source_dir), f"{source_dir} is not a directory."
assert os.path.isdir(replica_dir), f"{replica_dir} is not a directory."

files_source = os.listdir(source_dir)

print(f"These are the files at {source_dir}:")
for file in files_source:
    print(file)
    source_dir_path = os.path.join(source_dir, file)
    replica_dir_path = os.path.join(replica_dir, file)
    shutil.copy(source_dir_path, replica_dir_path)

print(
    f"All the files at {source_dir} have been copied to {replica_dir}.")

files_replica = os.listdir(replica_dir)

print(f"These are the files at {replica_dir}:")
for file in files_replica:
    print(file)
