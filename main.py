from flask import Flask, request

app = Flask(__name__)

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
    robots[robot_id] = request.remote_addr
    return 'OK'

if __name__ == '__main__':
    app.run(host='192.168.0.6', port=8080, debug=True)