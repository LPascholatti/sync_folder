import time
import config_log
import synchronization
import config


def main():
    print("This script will synchronise a source and replica directories.")

    config_log.configure_logging()

    source_dir = config.configure_source()
    replica_dir = config.configure_replica()

    interval = int(
        input("Add interval (number in seconds) for this synchronization: "))

    while True:
        synchronization.synchronise_directories(source_dir, replica_dir)
        print(f"Waiting for {interval} seconds...")
        time.sleep(interval)


if __name__ == "__main__":
    main()
