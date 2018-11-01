'''
Simplified version of a WSGI application with eventlet.
Does not have multi-process support.

Responds to HTTP requests.

Originally from:
http://eventlet.net/doc/examples.html#wsgi-server
'''

import eventlet
from eventlet import wsgi

SERVER_HOSTNAME = ''
SERVER_PORT = 6000

# This is a minimal WSGI application.
def application(env, start_response):
    response_body = 'Hello, World!\n'.encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))),
    ]
    # For reasons I have not researched, the WSGI standard (PEP 3333)
    # states that applications must call the server's callback
    # with the status and headers, then return the response body.
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    server_socket = eventlet.listen((SERVER_HOSTNAME, SERVER_PORT))
    # Eventlet provides a WSGI server.
    # This accepts a server socket (must already be listening)
    # and a WSGI application.
    wsgi.server(server_socket, application)
