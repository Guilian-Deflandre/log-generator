from src import constants
import datetime

class Log():
    def __init__(self, timestamp = None):
        self.timestamp = datetime.datetime.now() if (timestamp is None) else \
                            timestamp    
    def writeLog(self):
        file = open(constants.LOG_FILE_NAME, "a+")
        file.write(self.str() + "\n")
        file.close()

    def str(self):
        return self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z") + " " + \
                self.description
