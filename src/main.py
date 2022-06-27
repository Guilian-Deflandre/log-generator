from src import constants
from src.logger import Logger

"""
The Log Generator application simulate the logging behavior of an infra-
structure by generating typical logs following standard format into a log file.
This application is multi-threaded, each thread is responsible of creating and
write logs of different format into the output file. The different log formats
are defined in the log_generators package. The constants file of the application
made it fully configurable.

See: https://github.com/Guilian-Deflandre/log-generator
"""

def main():
    threads = []
    for i in range(constants.NUMBER_OF_THREAD):
        thread = Logger(i)
        threads.append(thread)
        thread.start()
    return

if __name__ == "__main__":
    main()