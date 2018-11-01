'''
Echo server using a the built-in eventlet server and a green thread pool.
Sends data directly over the socket (no HTTP).
A modification of: http://eventlet.net/doc/examples.html#socket-connect
'''

import eventlet

LISTEN_ADDRESS = '0.0.0.0'
LISTEN_PORT = 8090
MAX_THREADS = 10000
BUFFER_SIZE = 1024

def echo(client):
    print('Connected to client at: {}', client.getpeername())
    while True:
        c = client.recv(BUFFER_SIZE)
        if not c:
            break
        client.sendall(c)
    print('Client connction lost')

server = eventlet.listen((LISTEN_ADDRESS, LISTEN_PORT))
print('Server listening at: {}'.format(server.getsockname()))

# Create a pool of green threads. Specify the max number.
pool = eventlet.GreenPool(MAX_THREADS)
while True:
    # Wait for client connections
    new_client, address = server.accept()

    # Spawn a new thread for each client connection.
    # Spawn without return value. Use if you don't care why the thread exits.
    pool.spawn_n(echo, new_client)
