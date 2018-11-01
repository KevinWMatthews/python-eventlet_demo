'''Sample eventlet client.
Uses eventlet's green sockets.
'''

import eventlet
from eventlet.green import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8090
BUFFER_SIZE = 1024

messages = [
    'This client performs basic IO over a socket.',
    'Alternatively, connect from the command line:',
    '$ telnet localhost 8090',
]

with socket.socket() as sock:
    sock.connect((SERVER_ADDRESS, SERVER_PORT))
    print('Connected to server at: {}'.format(sock.getpeername()))
    responses = []
    for message in messages:
        print(message)
        sock.send(message.encode('utf-8'))
        response = sock.recv(BUFFER_SIZE)
        print(response.decode('utf-8'))
