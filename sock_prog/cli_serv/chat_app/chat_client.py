'''chat_client.py.'''

import sys
import socket
import select

def chat_client():
    '''Client.'''
    if len(sys.argv) < 3:
        print("Usage : python chat_client.py hostname port")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(2)

    # connect to remote host
    try:
        soc.connect((host, port))
    #pylint: disable=bare-except
    except:
        print("Unable to connect")
        sys.exit()

    print("Connected to remote host. You can start sending messages")
    sys.stdout.write('[Me] ')
    sys.stdout.flush()

    while 1:
        socket_list = [sys.stdin, soc]

        # Get the list sockets which are readable
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [])
        print(ready_to_write, in_error)

        for sock in ready_to_read:
            if sock == soc:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data:
                    print("\nDisconnected from chat server")
                    sys.exit()
                else:
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] ')
                    sys.stdout.flush()

            else:
                # user entered a message
                msg = sys.stdin.readline()
                soc.send(msg)
                sys.stdout.write('[Me] ')
                sys.stdout.flush()


if __name__ == "__main__":

    sys.exit(chat_client())
