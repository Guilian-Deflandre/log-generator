import unittest

from pygrok import Grok
from src.logs_generators.application_log import ApplicationLog

class UnitTest(unittest.TestCase):
    def test_grok_application_log(self):
        log = "2022-04-05T15:05:25+00:00 DEBUG [InternalWeb.com.Transaction.Manager]: Starting transaction for session 27ecbf1bc43079e72418d923cfb10dfc6a83970c"
        pattern = "%{TIMESTAMP_ISO8601:time} %{LOGLEVEL:logLevel} \[%{GREEDYDATA:app}\]: %{GREEDYDATA:logMessage}"
        grok = Grok(pattern)
        match = grok.match(log)
        self.assertTrue((match["time"] == "2022-04-05T15:05:25+00:00") and 
                        (match["logLevel"] == "DEBUG") and
                        (match["app"] == "InternalWeb.com.Transaction.Manager") and
                        (match["logMessage"]) == "Starting transaction for session 27ecbf1bc43079e72418d923cfb10dfc6a83970c")
    # Same for the others

if __name__ == '__main__':
    unittest.main()