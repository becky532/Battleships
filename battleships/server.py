from flask_socketio import SocketIO
from flask import Flask, request
from gameBack import Board

server = Flask(__name__)
server.config['SECRET_KEY'] = 'TeamTitanic'
socketio = SocketIO(server, cors_allowed_origins='*')


@socketio.on('connect')
def connect():
    sid = request.sid
    print(sid + ' connected!')
    userID = ''
    for index, user in enumerate(users):
        if user is None:
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
    row = boat[0][1]
    col = boat[0][1]
    print(sid)
    validPlacement = True
    socketio.emit('shipCheck', validPlacement, to=sid)


@socketio.on('readyCheck')
def readyCheck():
    if None not in users:       # checks that there are two users connected
        # board = Board.instance()
        sid = request.sid
        playerId = users.index(sid)
        if playerId == 0:
            otherId = 1
        else:
            otherId = 0
        # backend ready is true
        ready = True
        if ready:
            socketio.emit('personalReady', playerId, to=users[playerId])
            socketio.emit('enemyReady', playerId, to=users[otherId])

@socketio.on('attack')
def attack(coord):
    sid = request.sid
    playerId = users.index(sid)
    # turnToAttack(playerId)
    # validCoord(playerId, coord)
    turnToAttack = True
    validCoord = True
    if turnToAttack and validCoord:
        if playerId == 0:
            otherId = 1
        else:
            otherId = 0
        # attack player board and return result
        attackResult = False
        socketio.emit('attackResult', (attackResult, coord), to=users[playerId])
        socketio.emit('defenceResult', (attackResult, coord), to=users[otherId])


def main():
    board = Board.instance()
    board.initialise()
    print("Server has started!")
    socketio.run(server, port=5555)


if __name__ == "__main__":
    users = [None, None]
    main()

