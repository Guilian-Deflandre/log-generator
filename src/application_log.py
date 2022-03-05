import constants
from log import Log

class ApplicationLog(Log):
    def __init__(self, app_name, description, 
                 level = constants.LOG_LEVELS_STRING[constants.LOG_DEBUG_LEVEL]
                ) -> None:
        super().__init__(description)
        self.app_name = app_name
        self.level = level

    def str(self):
        return self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z") + " " + \
                self.level + " [" + self.app_name + "]:" + self.description
