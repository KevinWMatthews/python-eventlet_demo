# Taken from the documentation: http://eventlet.net/doc/modules/websocket.html#eventlet.websocket.WebSocketWSGI
# And secondarily from this example: http://eventlet.net/doc/examples.html#websocket-server-example

import eventlet
from eventlet import wsgi
from eventlet import websocket

SERVER_HOSTNAME = '127.0.0.1'
SERVER_PORT = 8090

# To create a websocket server, decorate a function with WebSocketWSGI and
# use it as a WSGI application
# The decorator changes the number of arguments!
# Instead of passing cgi_environ and start_response, accept a websocket connection.
@websocket.WebSocketWSGI
def application(ws):
    ws.send('Hello, world!')

if __name__ == '__main__':
    listener = eventlet.listen((SERVER_HOSTNAME, SERVER_PORT))
    wsgi.server(listener, application)
