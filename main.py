from flask import Flask, request
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

robots = {}

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return 'Welcome to Manager initial page!'

@app.route('/robot/<robot_id>/address')
def get_robot_address(robot_id):
    """Gets the public IP used to connect to the robot."""
    return robots[robot_id]

@app.route('/register/<robot_id>', methods = ['POST'])
def register(robot_id):
    """Register the public IP of the robot."""
    if request.headers.getlist("X-Forwarded-For"):
    	ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
    	ip = request.remote_addr
    robots[robot_id] = ip
    return 'OK'

@sockets.route('/control')
def control(ws):
    while not ws.closed:
        message = ws.receive()
        if message is None:  # message is "None" if the client has closed.
            continue
        # Send the message to all clients connected to this webserver
        # process. (To support multiple processes or instances, an
        # extra-instance storage or messaging system would be required.)
        clients = ws.handler.server.clients.values()
        for client in clients:
            client.ws.send(message)

if __name__ == '__main__':
    print("""
This can not be run directly because the Flask development server does not
support web sockets. Instead, use gunicorn:

gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app

""")