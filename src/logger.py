import datetime
import random
import threading
import time

from application_log import *
from constants import *

class Logger(threading.Thread):
    def __init__(self, threadID):
        super(Logger, self).__init__()
        self.threadID = threadID
        self._birthday = datetime.datetime.now()

    def run(self):
        while(True):
            applog = ApplicationLog("MySecretApp.com.Transaction.Manager",
                                    "Starting transaction for session " +
                                    "Thread: " + str(self.threadID))
            applog.writeLog()
            time_sleep = random.uniform(constants.THREAD_SLEEP_TIME_MIN,
                                        constants.THREAD_SLEEP_TIME_MAX)
            time.sleep(time_sleep)

            if((datetime.datetime.now() - self._birthday).total_seconds() 
                    > 10):
                return
