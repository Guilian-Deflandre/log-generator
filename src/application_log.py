from pydoc import describe
import random
import utils
import constants
from log import Log

class ApplicationLog(Log):
    def __init__(self, app_name, description) -> None:
        super().__init__(description)
        self._description_generator = [
            self._generate_connection_log,
            self._generate_connection_unknow_user_log,
            self._generate_profile_update_log,
            self._generate_transaction_log
        ]
        self.app_name = app_name

    def _generate_connection_log(self):
        description = "User " + utils.generate_random_username() + \
                      " connected from " + utils.generate_random_ipv4_address()
        return constants.LOG_LEVELS_STRING[constants.LOG_INFO_LEVEL] + " [" + \
                self.app_name + ".com.Connection.Manager]: " + description

    def _generate_connection_unknow_user_log(self):
        description = "Unknow user " + utils.generate_random_username() + \
                      " tried to connect from " + utils.generate_random_ipv4_address()
        return constants.LOG_LEVELS_STRING[constants.LOG_INFO_LEVEL] + " [" + \
                self.app_name + ".com.Connection.Manager]: " + description

    def _generate_profile_update_log(self):
        description = "User " + utils.generate_random_username() + \
                      " connected update profil from " + \
                      utils.generate_random_ipv4_address()
        return constants.LOG_LEVELS_STRING[constants.LOG_ERROR_LEVEL] + " [" + \
                self.app_name + ".com.Profile.Manager]: " + description

    def _generate_transaction_log(self):
        description = "Starting transaction for session " + \
                        utils.generate_session_id()
        return constants.LOG_LEVELS_STRING[constants.LOG_DEBUG_LEVEL] + " [" + \
                self.app_name + ".com.Transaction.Manager]: " + description

    def str(self):
        description = random.choice(self._description_generator)
        return self.timestamp.astimezone().replace(microsecond=0).isoformat() \
                + " " + description()
