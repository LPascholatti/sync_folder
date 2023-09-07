import hashlib

# Function that calcualtes sha256 for the files:


def calculate_sha256(file_path):
    # Setup Hashlib:
    block_size = 65536
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            sha256_hash.update(data)
        return sha256_hash.hexdigest()
