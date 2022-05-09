import datetime
import random
import threading
import time

from src import constants
from src.logs_generators.cisco_ios_log import CiscoIOSLog
from src.logs_generators.application_log import ApplicationLog
from src.logs_generators.ssh_authentication_log import SSHAuthenticationLogs

class Logger(threading.Thread):
    def __init__(self, threadID):
        super(Logger, self).__init__()
        self.threadID = threadID
        self._birthday = datetime.datetime.now()
        self._applog = ApplicationLog("InternalWeb")
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
            if(random.random() < constants.PROBABILITY_LOGGING_APPLICATION):
                self._applog.writeLog()
