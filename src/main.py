from log import *
from logger import Logger

def main():
    # Create new threads
    threads = []
    for i in range(constants.NUMBER_OF_THREAD):
        thread = Logger(i)
        threads.append(thread)
        thread.start()
    return

if __name__ == "__main__":
    main()