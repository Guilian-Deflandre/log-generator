import constants
import datetime

class Log():
    def __init__(self, description, timestamp = None):
        self.timestamp = datetime.datetime.now() if (timestamp is None) else timestamp
        self.description = description
    
    def writeLog(self):
        file = open(constants.LOG_FILE_NAME, "a")
        file.write(self.str() + "\n")
        file.close()

    def str(self):
        return self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z") + "" + self.description