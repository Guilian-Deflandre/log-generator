import unittest

from pygrok import Grok
from src.logs_generators.ssh_authentication_log import SSHAuthenticationLogs

class UnitTest(unittest.TestCase):
    def test_grok_ssh_authentication_log(self):
        log = "Apr 13 11:58:41 laptop-56.johnson.info sshd[1756]: Accepted password for lisahall from 46.129.166.13 port 51317 ssh2"
        pattern = "%{SYSLOGTIMESTAMP:syslog_timestamp} %{HOSTNAME:hostname} sshd\[%{INT:pid_sshd}\]: %{WORD:connexion_attempt_status} (user|password for)( invalid user)? %{USERNAME:username} from %{IPV4:sshd_remote_connection_ip}( port %{INT:sshd_remote_connection_port} %{GREEDYDATA})?$"
        grok = Grok(pattern)
        match = grok.match(log)
        self.assertTrue((match is not None) and
                        (match["syslog_timestamp"] == "Apr 13 11:58:41") and 
                        (match["hostname"] == "laptop-56.johnson.info") and
                        (match["pid_sshd"] == "1756") and
                        (match["connexion_attempt_status"] == "Accepted") and
                        (match["username"] == "lisahall") and
                        (match["sshd_remote_connection_ip"] == "46.129.166.13") and
                        (match["sshd_remote_connection_port"] == "51317"))
    
    def test_ssh_authentication_log_generated_log(self):
        logger = SSHAuthenticationLogs()
        pattern = "%{SYSLOGTIMESTAMP:syslog_timestamp} %{HOSTNAME:hostname} sshd\[%{INT:pid_sshd}\]: %{WORD:connexion_attempt_status} (user|password for)( invalid user)? %{USERNAME:username} from %{IPV4:sshd_remote_connection_ip}( port %{INT:sshd_remote_connection_port} %{GREEDYDATA})?$"
        grok = Grok(pattern)
        match = grok.match(logger.str())
        self.assertFalse(match is None)
    
    def test_ssh_authentication_log_generated_log__matched_field_length(self):
        logger = SSHAuthenticationLogs()
        pattern = "%{SYSLOGTIMESTAMP:syslog_timestamp} %{HOSTNAME:hostname} sshd\[%{INT:pid_sshd}\]: %{WORD:connexion_attempt_status} (user|password for)( invalid user)? %{USERNAME:username} from %{IPV4:sshd_remote_connection_ip}( port %{INT:sshd_remote_connection_port} %{GREEDYDATA})?$"
        grok = Grok(pattern)
        match = grok.match(logger.str())
        self.assertEqual(len(match), 7)
    
    def test_ssh_authentication_log_generated_log_matched_fields(self):
        logger = SSHAuthenticationLogs()
        pattern = "%{SYSLOGTIMESTAMP:syslog_timestamp} %{HOSTNAME:hostname} " \
                  "sshd\[%{INT:pid_sshd}\]: %{WORD:connexion_attempt_status} " \
                  "(user|password for)( invalid user)? %{USERNAME:username} " \
                  "from %{IPV4:sshd_remote_connection_ip}( port " \
                  "%{INT:sshd_remote_connection_port} %{GREEDYDATA})?$"
        grok = Grok(pattern)
        match = grok.match(logger.str())
        expected_keys_matched = ['syslog_timestamp', 'hostname', 'pid_sshd', 
                                 'connexion_attempt_status', 'username', 
                                 'sshd_remote_connection_ip', 
                                 'sshd_remote_connection_port']
        union = set(match.keys()).union(set(expected_keys_matched))
        intersection = set(match.keys()).intersection(set(expected_keys_matched))
        self.assertEqual(len(list(union - intersection)), 0)

if __name__ == '__main__':
    unittest.main()