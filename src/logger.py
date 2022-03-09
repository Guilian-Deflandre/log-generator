import datetime
import random
import threading
import time

from application_log import *
from cisco_ios_log import CiscoIOSLog
from constants import *
from ssh_authentication_log import SSHAuthenticationLogs

class Logger(threading.Thread):
    def __init__(self, threadID):
        super(Logger, self).__init__()
        self.threadID = threadID
        self._birthday = datetime.datetime.now()
        self._applog = ApplicationLog("MySecretApp.com.Transaction.Manager",
                                    "Starting transaction for session ")
        self._ciscoIOSLog = CiscoIOSLog()
        self._ssh_authentication_log = SSHAuthenticationLogs()

    def run(self):
        while(True):
            time_sleep = random.uniform(constants.THREAD_SLEEP_TIME_MIN,
                                        constants.THREAD_SLEEP_TIME_MAX)
            time.sleep(time_sleep)

            if(random.random() < constants.PROBABILITY_LOGGING_SSH_AUTH):
                self._ssh_authentication_log.writeLog()
            if(random.random() < constants.PROBABILITY_LOGGING_CISCO_IOS):
                self._ciscoIOSLog.writeLog()

            self._applog.writeLog()
            
            
            if((datetime.datetime.now() - self._birthday).total_seconds() 
                    > 10):
                return
