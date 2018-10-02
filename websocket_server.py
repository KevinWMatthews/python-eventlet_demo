# Work on this example: http://eventlet.net/doc/examples.html#websocket-server-example
import eventlet
from eventlet import wsgi
from eventlet import websocket

SERVER_HOSTNAME = '127.0.0.1'
SERVER_PORT = 8090

def application(environ, start_response):
    response_body = ''.encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    listener = eventlet.listen((SERVER_HOSTNAME, SERVER_PORT))
    wsgi.server(listener, application)
