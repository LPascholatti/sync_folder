import os
import logging
import hashing
import shutil


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
        hash_file = hashing.calculate_sha256(source_dir_path)
        source_hashes[file] = hash_file
        file_info = {"name": source_dir_path, "hash": hash_file}
        source_dict[file] = file_info

    # Iterate through replica directory and calculate hash, adds to dictionary.
    for file in files_replica:
        replica_dir_path = os.path.join(replica_dir, file)
        hash_file = hashing.calculate_sha256(replica_dir_path)
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
