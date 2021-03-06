# -*- coding: utf-8 -*-

import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.bitsight.parser import BitsightParserBot

EXAMPLE_REPORT = {"feed.url": "http://alerts.bitsighttech.com:8080/stream?",
                  "feed.accuracy": 100.0,
                  "__type": "Report",
                  "feed.name": "BitSight",
                  "raw": "eyJ0cm9qYW5mYW1pbHkiOiJTYWxpdHlwMnAiLCJlbnYiOnsicmV"
                         "tb3RlX2FkZHIiOiIxNTIuMTY2LjExOS4yIiwicmVtb3RlX3Bvcn"
                         "QiOiI2NTExOCIsInNlcnZlcl9hZGRyIjoiNTIuMTguMTk2LjE2O"
                         "SIsInNlcnZlcl9wb3J0IjoiOTc5NiJ9LCJfdHMiOjE0NjExMDc3"
                         "NjgsIl9nZW9fZW52X3JlbW90ZV9hZGRyIjp7ImNvdW50cnlfbmF"
                         "tZSI6IkRvbWluaWNhbiBSZXB1YmxpYyJ9fQ==",
                  "time.observation": "2016-04-19T23:16:08+00:00"
                  }

EXAMPLE_EVENT  = {"classification.type": "malware",
                  "destination.port": 9796,
                  "feed.accuracy": 100.0,
                  "destination.ip": "52.18.196.169",
                  "malware.name": "salityp2p",
                  "event_description.text": "Sinkhole attempted connection",
                  "time.source": "2016-04-19T23:16:08+00:00",
                  "source.ip": "152.166.119.2",
                  "feed.url": "http://alerts.bitsighttech.com:8080/stream?",
                  "source.geolocation.country": "Dominican Republic",
                  "time.observation": "2016-04-19T23:16:08+00:00",
                  "source.port": 65118, "__type": "Event",
                  "feed.name": "BitSight",
                  "raw": "eyJ0cm9qYW5mYW1pbHkiOiJTYWxpdHlwMnAiLCJlbnYiOnsic"
                  "mVtb3RlX2FkZHIiOiIxNTIuMTY2LjExOS4yIiwicmVtb3RlX3"
                  "BvcnQiOiI2NTExOCIsInNlcnZlcl9hZGRyIjoiNTIuMTguMTk"
                  "2LjE2OSIsInNlcnZlcl9wb3J0IjoiOTc5NiJ9LCJfdHMiOjE0"
                  "NjExMDc3NjgsIl9nZW9fZW52X3JlbW90ZV9hZGRyIjp7ImNvd"
                  "W50cnlfbmFtZSI6IkRvbWluaWNhbiBSZXB1YmxpYyJ9fQ=="
                  }

EXAMPLE_REPORT2 = {"feed.name": "BitSight",
                   "feed.accuracy": 100.0,
                   "feed.url": "http://alerts.bitsighttech.com:8080/stream?",
                   "raw": "eyJ0cm9qYW5mYW1pbHkiOiJTcHlBcHAiLCJlbnYiOnsicmVtb"
                          "3RlX3BvcnQiOiI1Mjg4OCIsInNlcnZlcl9uYW1lIjoiZGV2LX"
                          "VwZGF0ZS5pbmZvIiwic2VydmVyX2FkZHIiOiIxOTUuMjIuMjg"
                          "uMTk2IiwicmVxdWVzdF9tZXRob2QiOiJQT1NUIiwicmVtb3Rl"
                          "X2FkZHIiOiIxOTAuMTI0LjY3LjIxMSIsInNlcnZlcl9wb3J0I"
                          "joiODAifSwiX3RzIjoxNDYxMTA3NzU0LCJfZ2VvX2Vudl9yZW"
                          "1vdGVfYWRkciI6eyJjb3VudHJ5X25hbWUiOiJEb21pbmljYW4"
                          "gUmVwdWJsaWMifX0=",
                   "__type": "Report",
                   "time.observation":
                   "2016-04-19T23:16:10+00:00"
                   }

EXAMPLE_EVENT2  = {"feed.name": "BitSight",
                   "malware.name": "spyapp",
                   "destination.fqdn": "dev-update.info",
                   "source.ip": "190.124.67.211",
                   "destination.ip": "195.22.28.196",
                   "__type": "Event",
                   "source.geolocation.country": "Dominican Republic",
                   "time.source": "2016-04-19T23:15:54+00:00",
                   "source.port": 52888,
                   "time.observation": "2016-04-19T23:16:10+00:00",
                   "extra": "{\"request_method\": \"POST\"}",
                   "feed.url": "http://alerts.bitsighttech.com:8080/stream?",
                   "destination.port": 80,
                   "feed.accuracy": 100.0,
                   "raw": "eyJ0cm9qYW5mYW1pbHkiOiJTcHlBcHAiLCJlbnYiOnsicmVt"
                          "b3RlX3BvcnQiOiI1Mjg4OCIsInNlcnZlcl9uYW1lIjoiZGV2"
                          "LXVwZGF0ZS5pbmZvIiwic2VydmVyX2FkZHIiOiIxOTUuMjIu"
                          "MjguMTk2IiwicmVxdWVzdF9tZXRob2QiOiJQT1NUIiwicmVt"
                          "b3RlX2FkZHIiOiIxOTAuMTI0LjY3LjIxMSIsInNlcnZlcl9w"
                          "b3J0IjoiODAifSwiX3RzIjoxNDYxMTA3NzU0LCJfZ2VvX2Vu"
                          "dl9yZW1vdGVfYWRkciI6eyJjb3VudHJ5X25hbWUiOiJEb21p"
                          "bmljYW4gUmVwdWJsaWMifX0=",
                   "classification.type": "malware",
                   "event_description.text": "Sinkhole attempted connection"
                   }


class TestBitsightParserBot(test.BotTestCase, unittest.TestCase):

    @classmethod
    def set_bot(cls):
        cls.bot_reference = BitsightParserBot
        cls.default_input_message = EXAMPLE_REPORT

    def test_event(self):
        """ Test: report without fqdn """
        self.run_bot()

        self.assertMessageEqual(0, EXAMPLE_EVENT)

    def test_with_fqdn(self):
        """ Test: report with fqdn """
        self.input_message = EXAMPLE_REPORT2
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
