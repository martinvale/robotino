"""
This script runs the robotinomanager application using a development server.
"""

from os import environ
from robotinomanager import app, socketio

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '192.168.0.7')
    try:
        PORT = int(environ.get('SERVER_PORT', '8081'))
    except ValueError:
        PORT = 5555
    print("Server listening on: http://" + str(HOST) + ":" + str(PORT))
    #app.run(HOST, PORT)
    socketio.run(app, HOST, PORT)
    #import logging
    #app.logger.setLevel(logging.DEBUG)

    #from gevent import pywsgi
    #from geventwebsocket.handler import WebSocketHandler

    #server = pywsgi.WSGIServer((HOST, PORT), app, handler_class=WebSocketHandler)
    #server.serve_forever()