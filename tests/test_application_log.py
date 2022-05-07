import unittest

from pygrok import Grok
from src.logs_generators.application_log import ApplicationLog

class UnitTest(unittest.TestCase):

    pattern = "%{TIMESTAMP_ISO8601:time} %{LOGLEVEL:logLevel} " \
              "\[%{GREEDYDATA:app}\]:%{GREEDYDATA:logMessage}"

    def test_grok_application_log(self):
        log = "2022-04-13T11:58:41+00:00 INFO [InternalWeb.com.Profile." \
              "Manager]: User lisa84 update profil from 223.103.179.11"
        grok = Grok(self.pattern)
        match = grok.match(log)
        self.assertTrue((match is not None) and
                        (match["time"] == "2022-04-13T11:58:41+00:00") and 
                        (match["logLevel"] == "INFO") and
                        (match["app"] == "InternalWeb.com.Profile.Manager") and
                        (match["logMessage"] == " User lisa84 update profil " \
                            "from 223.103.179.11"))
    
    def test_application_log_generated_log(self):
        logger = ApplicationLog("App_Test")
        grok = Grok(self.pattern)
        match = grok.match(logger.str())
        self.assertFalse(match is None)
    
    def test_application_log_generated_log_matched_field_length(self):
        logger = ApplicationLog("App_Test")
        grok = Grok(self.pattern)
        match = grok.match(logger.str())
        self.assertEqual(len(match), 4)
    
    def test_application_log_generated_log_matched_fields(self):
        logger = ApplicationLog("App_Test")
        grok = Grok(self.pattern)
        match = grok.match(logger.str())
        expected_keys_matched = ['time', 'logLevel', 'app', 'logMessage']
        union = set(match.keys()).union(set(expected_keys_matched))
        intersection = set(match.keys()).intersection(set(expected_keys_matched))
        self.assertEqual(len(list(union - intersection)), 0)

if __name__ == '__main__':
    unittest.main()