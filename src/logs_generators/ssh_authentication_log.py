import random
import src.utils as utils
from src.logs_generators.log import *

class SSHAuthenticationLogs(Log):
    """
    TODO

    Attributes
    ----------
    _LOG_PROCESS : str
        The constant SSH process generating the log. Because we only focus on
        authentication here, it is made of a single process name. But others
        can be found from the SSH namely sudo, useradd, groupadd.

    Methods
    -------
    str()
        Generate a random log simulating an authentication to a host using SSH.
    """
    _LOG_PROCESS = "sshd"
    
    def __init__(self) -> None:
        super().__init__()

    def _generate_log(self):
        """TODO

        Parameters
        ----------
        

        Returns
        -------
        
        """
        host = utils.generate_random_hostname()
        username = utils.generate_random_username()
        ip_address = utils.generate_random_ipv4_address()
        port_number = str(utils.generate_random_port_number())
        pid = random.randint(1, 32768)
        status = random.choice(["Failed", "Accepted", "Invalid"])

        if(status == "Invalid"):
            return host + " " + self._LOG_PROCESS + "[" + str(pid) + "]: " + \
                   status + " user " + username + " from " + ip_address
        elif(status == "Failed"):
            return host + " " + self._LOG_PROCESS + "[" + str(pid) + "]: " + \
                   status + " password for " + \
                   random.choice(["invalid user ", ""]) + status + username + \
                   " from " + ip_address + " port " + port_number + " ssh2"
        
        return host + " " + self._LOG_PROCESS + "[" + str(pid) + "]: " + \
               status + " password for " + username + " from " + ip_address + \
               " port " + port_number + " ssh2"

    def str(self):
        """Generate a random log simulating an authentication to a host using
        SSH. This is based on log given in https://www.elastic.co/blog/grokking-
        the-linux-authorization-logs.

        Parameters
        ----------
        /

        Returns
        -------
        str
            A random SSH authentication log.
        
        """

        return self.timestamp.strftime("%b %d %H:%M:%S") + " " + \
               self._generate_log()
