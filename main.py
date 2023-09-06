import os
import shutil
import time
import logging
import hashlib

print("This script will synchronise a source and replica directories.")

# Input source and replica paths here:
source_dir = input("Please input the path of your source directory here: ")

replica_dir = input("Please input the path of your replica directory here: ")

# Configure logging:
log_file = input(
    f"Please enter the log file path and name.txt: ").lower()
print(f"You chose: {log_file}")

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Setup Hashlib:
hash_algorithm = 'sha256'
block_size = 65536
sha256_hash = hashlib.sha256()

# Function that calcualtes sha256 for the files:


def calculate_sha256(file_path):
    with open(file_path, "rb") as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            sha256_hash.update(data)
        return sha256_hash.hexdigest()


# Create dir for source in case it does not exist:
if not os.path.isdir(source_dir):
    os.makedirs(source_dir)
    print(f"Directory {source_dir} has been created.")
    logging.info(f"Directory {source_dir} has been created.")
else:
    print(f"The directory {source_dir} exists.")

print(f"The source directory is: {source_dir}")
logging.info(f"The source directory is: {source_dir}")

# Create dir for replica in case it does not exist:
if not os.path.isdir(replica_dir):
    os.makedirs(replica_dir)
    print(f"Directory {replica_dir} has been created.")
    logging.info(f"Directory {replica_dir} has been created.")
else:
    print(f"The directory {replica_dir} exists.")

print(f"The replica directory is: {replica_dir}")
logging.info(f"The replica directory is: {replica_dir}")

interval = int(input("Add interval (number) for this synchronization: "))


def synchronise_directories(source_dir, replica_dir):
    # List directories using os:
    files_source = os.listdir(source_dir)
    files_replica = os.listdir(replica_dir)

    # Print source path:
    print(f"These are the files at {source_dir}:\n {files_source}")
    logging.info(f"These are the files at {source_dir}:\n {files_source}")

    source_hashes = {}
    replica_hashes = {}

    source_dict = {}
    replica_dict = {}

    # Iterate through source directory and calculate hash, adds to dictionary.
    for file in files_source:
        source_dir_path = os.path.join(source_dir, file)
        hash_file = calculate_sha256(source_dir_path)
        source_hashes[file] = hash_file
        file_info = {"name": source_dir_path, "hash": hash_file}
        source_dict[file] = file_info

    # Iterate through replica directory and calculate hash, adds to dictionary.
    for file in files_replica:
        replica_dir_path = os.path.join(replica_dir, file)
        hash_file = calculate_sha256(replica_dir_path)
        replica_hashes[file] = hash_file
        file_info = {"name": replica_dir_path, "hash": hash_file}
        replica_dict[file] = file_info

    different_files = []
    diff_files_dic = {}
    for file, hash in source_dict.items():
        replica_hash = replica_hashes.get(file)
        if hash != replica_hash:
            different_files.append(file)
            file_info = {"name": file, "hash": hash}
            diff_files_dic[file] = file_info

    print(
        f"The different files to be copied from the source directory are: {diff_files_dic}")
    logging.info(
        f"The different files to be copied from the source directory are: {diff_files_dic}")

    missing_files = []
    missing_files_dic = {}
    for file, hash in replica_dict.items():
        source_hash = source_hashes.get(file)
        if hash != source_hash:
            missing_files.append(file)
            file_info = {"name": file, "hash": hash}
            missing_files_dic[file] = file_info

    print(
        f"The missing files to be removed from the replica directory are: {missing_files_dic}")
    logging.info(
        f"The missing files to be removed from the replica directory are: {missing_files_dic}")

    # Copy files to replica directory
    for file in different_files:
        # print(file)
        source_dir_path = os.path.join(source_dir, file)
        replica_dir_path = os.path.join(replica_dir, file)
        shutil.copy2(source_dir_path, replica_dir_path)
        logging.info(f"Copied {file} to replica folder {replica_dir}")

    print(
        f"All the different files at {source_dir} have been copied to {replica_dir}.")

    # Delete files missing at source
    for file in missing_files:
        replica_dir_path = os.path.join(replica_dir, file)
        os.remove(replica_dir_path)
        logging.info(f"Removed {file} from replica folder {replica_dir}")

    print(
        f"All the different files at {replica_dir} have been deleted.")

    files_replica_updated = os.listdir(replica_dir)
    print(f"These are the files at {replica_dir}:")
    for file in files_replica_updated:
        print(file)


while True:
    synchronise_directories(source_dir, replica_dir)
    print(f"Waiting for {interval} seconds...")
    time.sleep(interval)
