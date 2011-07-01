import os
import unittest
import uuid

from nimboss.ctx import ContextClient, BrokerAuthError, ContextNotFoundError

BROKER_URL = "https://nimbus.ci.uchicago.edu:8888/ContextBroker/ctx/"

class ContextClientTests(unittest.TestCase):

    # right now these tests bump against a real broker. This should be replaced
    # with a mockout httplib2.Http with controlled responses

    def setUp(self):
        self.key = os.environ['CTXBROKER_KEY']
        self.secret = os.environ['CTXBROKER_SECRET']

    def test_404(self):
        ctx = ContextClient(BROKER_URL, self.key, self.secret)
        try:
            ctx.get_status(BROKER_URL + str(uuid.uuid4()))
        except ContextNotFoundError, e:
            print "got error %s" % e
        else:
            self.fail("Expected error from broker")

    def test_403(self):
        ctx = ContextClient(BROKER_URL, self.key, self.secret + "thismakesitwrong")
        try:
            ctx.get_status(BROKER_URL + str(uuid.uuid4()))
        except BrokerAuthError, e:
            print "got error %s" % e
        else:
            self.fail("Expected error from broker")


