'''
Taken from the documentation:
http://eventlet.net/doc/modules/websocket.html
And from this example:
http://eventlet.net/doc/examples.html#websocket-server-example
'''

import eventlet
from eventlet import wsgi
from eventlet import websocket

SERVER_HOSTNAME = '127.0.0.1'
SERVER_PORT = 8090

@websocket.WebSocketWSGI
def application(ws):
    while True:
        # http://eventlet.net/doc/modules/websocket.html#eventlet.websocket.WebSocket.wait
        message = ws.wait()
        if message is None:
            break
        ws.send(message)

if __name__ == '__main__':
    listener = eventlet.listen((SERVER_HOSTNAME, SERVER_PORT))
    wsgi.server(listener, application)
