import eventlet

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 6000
# Reserve a pool of green threads. Default max = 1000.
pool = eventlet.GreenPool()

sock = eventlet.connect((SERVER_ADDRESS, SERVER_PORT))
print('Connected to server at: {}'.format(sock.getpeername()))

#TODO send data to the server
