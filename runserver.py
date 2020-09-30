"""
This script runs the robotinomanager application using a development server.
"""

from os import environ
from robotinomanager import app, sockets

if __name__ == '__main__':
    HOST = '192.168.0.7'
    PORT = 8081
    #HOST = environ.get('SERVER_HOST', '192.168.0.7')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '8081'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    #socketio.run(app, '192.168.0.7', 8081)
    import logging
    app.logger.setLevel(logging.DEBUG)

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer((HOST, PORT), app, handler_class=WebSocketHandler)
    print("Server listening on: http://" + str(HOST) + ":" + str(PORT))
    server.serve_forever()