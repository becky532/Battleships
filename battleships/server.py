from flask_socketio import SocketIO
from flask import Flask, request
from gameBack import Board
from gameMechanicsBackend import Game

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
    board = Board.instance()
    sid = request.sid
    playerId = users.index(sid)
    print(boat)
    row = 6 - boat[0][1]
    col = boat[0][0]
    shipType = boat[1].title()
    validPlacement = board.placeShip(row, col, shipType, playerId)
    socketio.emit('shipCheck', validPlacement, to=sid)


@socketio.on('readyCheck')
def readyCheck():
    if None not in users:       # checks that there are two users connected
        board = Board.instance()
        sid = request.sid
        playerId = users.index(sid)
        otherId = getOtherId(playerId)
        ready = board.checkAllPiecesPlaced(playerId)
        if ready:
            socketio.emit('personalReady', playerId, to=users[playerId])
            socketio.emit('enemyReady', playerId, to=users[otherId])


@socketio.on('attack')
def attack(coord):
    board = Board.instance()
    game = Game(board)
    sid = request.sid
    playerId = users.index(sid)
    row = 6 - coord[0][1]
    col = coord[0][0]
    alreadyHit = board.checkDuplicateAttack(row, col, playerId)
    if not alreadyHit:
        attackData = game.fire(row, col, playerId)
        if attackData is not None:
            validCoord = attack[0]
            attackResult = attack[1]
            if validCoord:
                otherId = getOtherId(playerId)
                # attack player board and return result
                socketio.emit('attackResult', (attackResult, coord), to=users[playerId])
                socketio.emit('defenceResult', (attackResult, coord), to=users[otherId])

            #if statement checking game over, if true broadcast victory page?


@socketio.on('removeBoatIfOnBoard')
def attack(shipName):
    board = Board.instance()
    sid = request.sid
    playerId = users.index(sid)
    shipName = shipName.title()
    board.remove(shipName, playerId)


def getOtherId(playerId):
    if playerId == 0:
        otherId = 1
    else:
        otherId = 0
    return otherId


def main():
    board = Board.instance()
    board.initialise()
    print("Server has started!")
    socketio.run(server, port=5555)


if __name__ == "__main__":
    users = [None, None]
    main()

