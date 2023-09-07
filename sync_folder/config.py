import os
import logging


def configure_source():
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

    return source_dir


def configure_replica():
    replica_dir = input(
        "Please input the path of your replica directory here: ")

    # Create dir for replica in case it does not exist:
    if not os.path.isdir(replica_dir):
        os.makedirs(replica_dir)
        print(f"Directory {replica_dir} has been created.")
        logging.info(f"Directory {replica_dir} has been created.")
    else:
        print(f"The directory {replica_dir} exists.")

    print(f"The replica directory is: {replica_dir}")
    logging.info(f"The replica directory is: {replica_dir}")

    return replica_dir
