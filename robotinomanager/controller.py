from flask_socketio import send, emit
from robotinomanager import socketio

@socketio.on('command request')
def command_request(message):
    print('command request: ' + message)
    emit('my response', {'command': message}, broadcast=True)

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def connect():
    print('connected!')
    #emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
