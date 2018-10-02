import eventlet

LISTEN_ADDRESS = '0.0.0.0'
LISTEN_PORT = 6000
MAX_THREADS = 10000

def echo(client):
    while True:
        c = client.recv(1)
        if not c:
            break
        client.sendall(c)

server = eventlet.listen((LISTEN_ADDRESS, LISTEN_PORT))
# Create a pool of green threads. Specify the max number.
pool = eventlet.GreenPool(MAX_THREADS)
while True:
    print('Listening: ({}:{})'.format(LISTEN_ADDRESS, LISTEN_PORT))
    new_sock, address = server.accept()
    # Spawn without return value. Use if you don't care why the thread exits.
    pool.spawn_n(echo, new_sock)
