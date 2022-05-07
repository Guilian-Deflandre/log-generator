import unittest

from pygrok import Grok
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

    pattern = "\*%{SYSLOGTIMESTAMP:syslog_timestamp} %{GREEDYDATA:facility}-" \
              "%{INT:severity_level}-%{GREEDYDATA:facility_mnemonic}: "\
              "%{GREEDYDATA:description}"

    def test_grok_cisco_ios_log(self):
        log = "*Apr 13 11:58:41.180 LINEPROTO-5-UPDOWN: Line protocol on " \
              "Interface GigabitEthernet0/2, changed state to up"
        grok = Grok(self.pattern)
        match = grok.match(log)
        self.assertTrue((match is not None) and
                        (match["syslog_timestamp"] == "Apr 13 11:58:41.180") and 
                        (match["facility"] == "LINEPROTO") and
                        (match["severity_level"] == "5") and
                        (match["facility_mnemonic"] == "UPDOWN") and
                        (match["description"] == "Line protocol on Interface "\
                            "GigabitEthernet0/2, changed state to up"))
    
    def test_cisco_ios_log_generated_log(self):
        logger = CiscoIOSLog()
        grok = Grok(self.pattern)
        match = grok.match(logger.str())
        self.assertFalse(match is None)
    
    def test_cisco_ios_log_generated_log__matched_field_length(self):
        logger = CiscoIOSLog()
        grok = Grok(self.pattern)
        match = grok.match(logger.str())
        self.assertEqual(len(match), 5)
    
    def test_cisco_ios_log_generated_log_matched_fields(self):
        logger = CiscoIOSLog()
        grok = Grok(self.pattern)
        match = grok.match(logger.str())
        expected_keys_matched = ['syslog_timestamp', 'facility',
                                 'severity_level', 'facility_mnemonic',
                                 'description']
        union = set(match.keys()).union(set(expected_keys_matched))
        intersection = set(match.keys()).intersection(set(expected_keys_matched))
        self.assertEqual(len(list(union - intersection)), 0)


if __name__ == '__main__':
    unittest.main()