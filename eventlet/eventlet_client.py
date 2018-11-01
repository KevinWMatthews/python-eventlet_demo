'''Sample eventlet client.
Uses eventlet's green sockets.
'''

import eventlet
from eventlet.green import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 6000

sock = socket.socket()
sock.connect((SERVER_ADDRESS, SERVER_PORT))
print('Connected to server at: {}'.format(sock.getpeername()))
