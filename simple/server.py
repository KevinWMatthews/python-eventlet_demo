import eventlet

LISTEN_ADDRESS = '0.0.0.0'
LISTEN_PORT = 6000
MAX_THREADS = 10000

def echo(client):
    print('Connected to client at: {}', client.getpeername())
    while True:
        c = client.recv(1)
        if not c:
            break
        client.sendall(c)
    print('Client connction lost')

server = eventlet.listen((LISTEN_ADDRESS, LISTEN_PORT))
print('Server listening at: {}'.format(server.getsockname()))

# Create a pool of green threads. Specify the max number.
pool = eventlet.GreenPool(MAX_THREADS)
while True:
    new_client, address = server.accept()
    # Spawn without return value. Use if you don't care why the thread exits.
    pool.spawn_n(echo, new_client)
