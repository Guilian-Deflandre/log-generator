import datetime
import random
import threading
import time

from src import constants
from src.logs_generators.cisco_ios_log import CiscoIOSLog
from src.logs_generators.application_log import ApplicationLog
from src.logs_generators.ssh_authentication_log import SSHAuthenticationLogs

class Logger(threading.Thread):
    """
    This class implements the Logger threads of the application, responsible of
    generating logs and output them into a log file. Each logger oscillate
    between its action phase where it create and write a log and its sleeping
    phase where it is in standby for a while.

    Attributes
    ----------
    _birthdate : timestamp
        The timestamp of the creation of the thread.
    _app_log : ApplicationLog
        The object forging typical application logs.
    _cisco_ios_log : CiscoIOSLogs
        The object forging typical IOS logs of Cisco devices.
    _ssh_authentication_log : SSHAuthenticationLogs
        The object forging typical authentication logs from SSH services.

    Methods
    -------
    run()
        Implements the infinite loop where the thread oscillate between its
        action and standby phases.
    """

    def __init__(self, threadID):
        super(Logger, self).__init__()
        self.threadID = threadID
        self._birthdate = datetime.datetime.now()
        self._app_log = ApplicationLog("InternalWeb")
        self._cisco_ios_log = CiscoIOSLog()
        self._ssh_authentication_log = SSHAuthenticationLogs()

    def run(self):
        while(True):
            time_sleep = random.uniform(constants.THREAD_SLEEP_TIME_MIN,
                                        constants.THREAD_SLEEP_TIME_MAX)
            time.sleep(time_sleep)

            if(random.random() < constants.PROBABILITY_LOGGING_SSH_AUTH):
                self._ssh_authentication_log.write_log()
            if(random.random() < constants.PROBABILITY_LOGGING_CISCO_IOS):
                self._cisco_ios_log.write_log()
            if(random.random() < constants.PROBABILITY_LOGGING_APPLICATION):
                self._app_log.write_log()
