import os
import shutil
import time
import logging

# Configure logging:
input_log_file = input(f"Please enter the log filename without .txt: ").lower()
log_file = f"./{input_log_file}.txt"
print(f"You chose: {log_file}")

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

print("This script will synchronise a source and replica directories.")

# Input source and replica paths here:
source_dir = input("Please input the path of your source directory here: ")

# Create dir for source in case it does not exist:
if not os.path.isdir(source_dir):
    os.makedirs(source_dir)
    print(f"Directory {source_dir} has been created.")
    logging.info(f"Directory {source_dir} has been created.")
else:
    print(f"The directory {source_dir} exists.")

print(f"The source directory is: {source_dir}")
logging.info(f"The source directory is: {source_dir}")

replica_dir = input("Please input the path of your replica directory here: ")

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

    # Create set from lists to get the difference in files between the two direcotires:
    source_set = set(files_source)
    replica_set = set(files_replica)

    # Differentiate files in both directories:
    diff_source_files = source_set - replica_set
    print(
        f"The following files are missing at {replica_dir}:\n {diff_source_files}")
    logging.info(
        f"The following files are missing at {replica_dir}:\n {diff_source_files}")

    diff_replica_files = replica_set - source_set
    print(
        f"The following files are missing at {source_dir}:\n {diff_replica_files}")
    logging.info(
        f"The following files are missing at {source_dir}:\n {diff_replica_files}")

    # Copy files to replica directory
    for file in diff_source_files:
        # print(file)
        source_dir_path = os.path.join(source_dir, file)
        replica_dir_path = os.path.join(replica_dir, file)
        shutil.copy2(source_dir_path, replica_dir_path)
        logging.info(f"Copied {file} to replica folder {replica_dir}")

    print(
        f"All the different files at {source_dir} have been copied to {replica_dir}.")

    # Delete files missing at source
    for file in diff_replica_files:
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
