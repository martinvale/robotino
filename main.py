from flask import Flask, request
from falsk_sockets import Sockets

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

@app.route('/control')
def control(ws):
	while not ws.closed:
		message = ws.receive()
		if message is None:
			continue
		print(message)

if __name__ == '__main__':
    app.run(host='192.168.0.6', port=8080, debug=True)