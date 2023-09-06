# Synchronise Files

### Requirements:
- Python
- Run it with `python main.py` in the script's directory.

This script aims to synchronise directory A with directory B.

Currently using `./source` and `./replica` as test directories.

- Inputs from the user a source and replica path from the command line.
- Inputs from the user a destionation path that should serve as a text log for the script's operations.
- In case the directories above do not exist, the script will create one for you.
- Inputs from the user an interval time in seconds in which the script should run.
- This script calculates the hash sha256 for all the files in a source directory and compare them with the files on a replica directory.
- Quit the program by typing `control + c`. The log will be preserved with all the changes.