import os
import shutil

# Source and replica paths here:
source_dir = "./source"
print(f"Your source file is: {source_dir}")
replica_dir = "./replica"
print(f"Your replica directory is: {replica_dir}")

# Assert that source and replica are directories:
assert os.path.isdir(source_dir), f"{source_dir} is not a directory."
assert os.path.isdir(replica_dir), f"{replica_dir} is not a directory."

# List directories using os:
files_source = os.listdir(source_dir)
files_replica = os.listdir(replica_dir)

# Print source path:
print(f"These are the files at {source_dir}:\n {files_source}")

# Create set from lists to get the difference in files between the two direcotires:
source_set = set(files_source)
replica_set = set(files_replica)

# Distinguish files in both directories:
diff_source_files = source_set - replica_set
print(
    f"The following files are missing at {replica_dir}:\n {diff_source_files}")

diff_replica_files = replica_set - source_set
print(
    f"The following files are missing at {source_dir}:\n {diff_replica_files}")

# Copy files to replica directory
for file in diff_source_files:
    # print(file)
    source_dir_path = os.path.join(source_dir, file)
    replica_dir_path = os.path.join(replica_dir, file)
    shutil.copy2(source_dir_path, replica_dir_path)

print(
    f"All the different files at {source_dir} have been copied to {replica_dir}.")

# Delete files missing at source
for file in diff_replica_files:
    replica_dir_path = os.path.join(replica_dir, file)
    os.remove(replica_dir_path)

print(
    f"All the different files at {replica_dir} have been deleted.")

files_replica_updated = os.listdir(replica_dir)
print(f"These are the files at {replica_dir}:")
for file in files_replica_updated:
    print(file)
