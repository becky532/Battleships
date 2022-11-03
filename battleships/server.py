from flask_socketio import SocketIO, send
from flask import Flask, request
from gameBack import Board

server = Flask(__name__)
server.config['SECRET_KEY'] = 'TeamTitanic'
socketio = SocketIO(server, cors_allowed_origins='*')
users = [None, None]
@socketio.on('message')
def handleMessage(msg):
    print(msg)
    # gameback function
    send(msg, broadcast=True) #player 2 sent (coord, if hit)

    # can we return data to player 1?


@socketio.on('connect')
def connect():
    sid = request.sid
    print(sid + ' connected!')
    userID = ''
    for index, user in enumerate(users):
        if user is None:
            userID = sid        # check userID '' later and disconnect connection if so
            users[index] = sid
            break


@socketio.on('disconnect')
def disconnect():
    sid = request.sid
    for index, user in enumerate(users):
        if user == sid:
            users[index] = None
    print(f'User ID {sid} disconnected')


@socketio.on('shipCheck')
def validMoveCheck(boat):
    sid = request.sid
    print(boat)
    print(sid)
    socketio.emit('shipCheck', to=sid)


if __name__ == "__main__":
    socketio.run(server, port=5555)

