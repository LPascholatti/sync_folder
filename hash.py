import hashlib
import os

hash_algorithm = 'sha256'
block_size = 65536
sha256_hash = hashlib.sha256()
file_path = "./source/file.txt"

# Input source and replica paths here:
source_dir = input("Please input the path of your source directory here: ")

replica_dir = input("Please input the path of your replica directory here: ")


def calculate_hash(file_path):
    hasher = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
        hasher.update(data)
    return hasher.hexdigest()


def calculate_sha256(file_path):
    with open(file_path, "rb") as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            sha256_hash.update(data)
        return sha256_hash.hexdigest()


calculate_hash(file_path)
calculate_sha256(file_path)

# List directories using os:
files_source = os.listdir(source_dir)
files_replica = os.listdir(replica_dir)
print(files_source)

source_hashes = []
replica_hashes = []

for file in files_source:
    source_dir_path = os.path.join(source_dir, file)
    hash_file = calculate_sha256(source_dir_path)
    source_hashes.append(hash_file)

for file in files_replica:
    replica_dir_path = os.path.join(replica_dir, file)
    hash_file = calculate_sha256(replica_dir_path)
    replica_hashes.append(hash_file)

hash_source_set = set(source_hashes)
print(hash_source_set)
hash_replica_set = set(replica_hashes)
print(hash_replica_set)

diff_hashes_source = hash_source_set - hash_replica_set
print(diff_hashes_source)

diff_hashes_replica = hash_replica_set - hash_source_set
print(diff_hashes_replica)
