"""Pytest module to test chat client."""
import os, sys
import unittest
import SocketServer

from mock import patch
from threading import Thread

HOSTNAME = '127.0.0.1'
PORT = 8081

C_DIR = os.getcwd()
SRC_DIR = '%s/../src/' % C_DIR

sys.path.append(SRC_DIR)
from client import ChatClient


class TestChatClient(unittest.TestCase):
    """Test module to test chat client."""

    @staticmethod
    def setup(self):
        """Setup Class."""
        client_patch = mock.patch.object(
            host=HOSTNAME, port=PORT, nickname=client1, autospec=True)

    def test_run(self):
        """Test run."""
        # self.ServObj = ServObj(('127.0.0.1', 8001), ReqHandler).serve_forever()
        # self.RequestHandler()
        self.ReqHandler.process_input()
        print("check point.")
        # self.CliObj = CliObj(host='127.0.0.1', port=8001, nickname='customer')
        # print(self.CliObj.output.write('/users\r\n'))
        '''readline = self.CliObj.input.readline().strip()
        print(readline)
        self.assertIn('customer', readline)'''


if __name__ == '__main__':
	unittest.main()
