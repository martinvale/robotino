"""
The flask application package.
"""

from flask import Flask
from flask_socketio import SocketIO
#from flask_sockets import Sockets

app = Flask(__name__)
socketio = SocketIO(app, ping_interval=20)
#sockets = Sockets(app)

import robotinomanager.views
import robotinomanager.controller
