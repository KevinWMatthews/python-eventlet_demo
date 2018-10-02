# A simplified version of: http://eventlet.net/doc/examples.html#socket-connect

import eventlet
from eventlet.green import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 6000

sock = socket.socket()
sock.connect((SERVER_ADDRESS, SERVER_PORT))
print('Connected to server at: {}'.format(sock.getpeername()))
