# Eventlet

Introduction to the eventlet library.
Uses green threads. Isn't this an M:N threading model?


## Background

Set up several examples of client/server pairs.

  * eventlet -> eventlet's server with a thread pool
  * wsgi -> eventlet's built-in wsgi server
  * websocket -> eventlet's websocket module

Examples are run on localhost, port 6000.


## Setup

Create a virtual environment
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


## Links:

[Design Patterns](eventlet.net/doc/design_patterns.html)


## TODO

Implement a [dispatch pattern](http://eventlet.net/doc/design_patterns.html#dispatch-pattern).
This is a proxy server.
