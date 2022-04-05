import unittest

from src.logs_generators.cisco_ios_log import CiscoIOSLog

_log_examples = ["SYS-5-CONFIG_I: Configured from console by console",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to up",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to up",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/3, changed state to up",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to down",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to down",
                "LINK-3-UPDOWN: Interface GigabitEthernet0/3, changed state to down",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to up",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/3, changed state to up",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to down",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to down",
                "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/3, changed state to down"]

class UnitTest(unittest.TestCase):
    def test_function_generate_log_cisco_ios(self):
        ciscoLogger = CiscoIOSLog()
        log = ciscoLogger._generate_log()
        if(log not in _log_examples):
            print(log)

        self.assertTrue(ciscoLogger._generate_log() in _log_examples)


if __name__ == '__main__':
    unittest.main()