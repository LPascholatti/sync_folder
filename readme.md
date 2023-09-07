# Synchronise Files

## Requirements

- Python
- Run it with `python main.py` in the `sync_folder` directory.

This script aims to synchronise directory A with directory B. With all changes in A reflecting to B, including deleting files in B that are not included at A

Currently using `./sync_folder/source` and `./sync_folder/replica` as test directories. The `./source` directory contains `.txt` files with dummy sentences for testing purposes.

## Sync Folders - File Structure

### config.py

- Inputs from the user a source and replica path from the command line.
- Inputs from the user a destionation path that should serve as a text log for the script's operations.
- In case the directories above do not exist, the script will create one for you.

### config_log.py

- Input from the user a path for the log file and config the `logging` package.

### hashing.py

- This function calculates the hash sha256 for a given file, it us used by the `synchronization` module when comparing source files with those existing on a replica directory.

### synchronization.py

- List all directories existing in the source and replica directories.
- Creates a dictionary with file and hash, that is added to the logs.
- Iterate over the diretories source and replica to catalogue what are different files that should be copied, based on hashing.
- Iterate over the directories source and replica to catalogue the missing files at source who will be removed, based on hashing.
- Copy and remove files to the replica directory.

### main.py

- Inputs from the user an interval time in seconds in which the script should run.
- Loops the synchronisation based on the interval input above.
- Quit the program by typing `control + c`. The log will be preserved with all the changes.