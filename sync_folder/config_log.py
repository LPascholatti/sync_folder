import logging


def configure_logging():
    log_file = input(
        f"Please enter the log file path and name.txt: ").lower()
    print(f"You chose: {log_file}")

    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')
