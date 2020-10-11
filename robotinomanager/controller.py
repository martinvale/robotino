from flask import request
from flask_socketio import send, emit
from robotinomanager import socketio

broadcaster_id = None

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
    print('{} connected!'.format(request.sid))
    #emit('my response', {'data': 'Connected'})

@socketio.on('broadcaster')
def broadcaster():
    global broadcaster_id
    broadcaster_id = request.sid;
    emit('broadcaster')

@socketio.on('watcher')
def watcher():
    emit('watcher', request.sid, room=broadcaster_id)

@socketio.on('disconnect')
def disconnect():
    print('Client {} disconnected'.format(request.sid))
    emit('disconnectPeer', {'data': 'sid'}, room=broadcaster_id)

@socketio.on('offer')
def offer(id, message):
    emit('offer', (request.sid, message), room=id)

@socketio.on('answer')
def answer(id, message):
    emit('answer', (request.sid, message), room=id)

@socketio.on('candidate')
def candidate(id, message):
    emit('candidate', (request.sid, message), room=id)