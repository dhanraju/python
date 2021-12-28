"""Chat Client."""
#!/usr/bin/python
import pwd
import socket
import sys
import os
from threading import Thread

HOSTNAME = '127.0.0.1'
PORT = 8081


class ClientError(Exception):
    """Client class Exception."""
    pass


#pylint: disable=too-few-public-methods
class ChatClient(object):
    """Chat Client Class."""
    def __init__(self, host, port, nickname):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.input_fd = self.socket.makefile('rb', 0)
        self.output = self.socket.makefile('wb', 0)

        #Send the given nickname to the server.
        auth_demand = self.input_fd.readline()
        if not auth_demand.startswith("Who are you?"):
            raise ClientError("This doesn't seem to be a Python Chat Server.")
        self.output.write(nickname + '\r\n')
        response = self.input_fd.readline().strip()
        if not response.startswith("Hello"):
            raise ClientError(response)
        print(response)
        #Start out by printing out the list of members.
        self.output.write('/users\r\n')
        print("Currently in the chat room:", self.input_fd.readline().strip())
        self.run()

    def run(self):
        """Start a separate thread to gather the input from the
        keyboard even as we wait for messages to come over the
        network. This makes it possible for the user to simultaneously
        send and receive chat text."""
        propagate_stdin = self.PropagateStandardInput(self.output)
        propagate_stdin.start()

        #Read from the network and print everything received to standard
        #output. Once data stops coming in from the network, it means
        #we've disconnected.
        #pylint: disable=redefined-variable-type
        input_text = True
        while input_text:
            input_text = self.input_fd.readline()
            if input_text:
                print(input_text.strip())
        propagate_stdin.done = True

    class PropagateStandardInput(Thread):
        """A class that mirrors standard input to the chat server
        until it's told to stop."""
        def __init__(self, output):
            """Make this thread a daemon thread, so that if the Python
            interpreter needs to quit it won't be held up waiting for this
            thread to die."""
            Thread.__init__(self)
            self.setDaemon(True)
            self.output = output
            self.done = False

        def run(self):
            """Echo standard input to the chat server until told to stop."""
            while not self.done:
                input_text = sys.stdin.readline().strip()
                if input_text:
                    self.output.write(input_text + '\r\n')


if __name__ == '__main__':
    # import sys
    #See if the user has an OS-provided 'username' we can use as a default
    #chat nickname. If not, they have to specify a nickname.
    try:
        # import pwd
        DEFAULT_NICKNAME = pwd.getpwuid(os.getuid())[0]
    except ImportError:
        DEFAULT_NICKNAME = None

    if len(sys.argv) < 2 or not DEFAULT_NICKNAME:
        print("Usage: %s [username]" % sys.argv[0])
        sys.exit(1)

    if len(sys.argv) > 1:
        NICKNAME = sys.argv[1]
    else:
        #We must be on a system with usernames, or we would have
        #exited earlier.
        NICKNAME = DEFAULT_NICKNAME

    ChatClient(HOSTNAME, PORT, NICKNAME)
