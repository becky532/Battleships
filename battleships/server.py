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
    board.printBoard(playerId)
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
    sid = request.sid
    playerId = users.index(sid)
    row = 6 - coord[1]
    col = coord[0]
    alreadyHit = board.checkDuplicateAttack(row, col, playerId)
    if not alreadyHit:
        attackData = game.fire(row, col, playerId)
        if attackData is not None:
            validCoord = attackData[0]
            attackResult = attackData[1]
            gameOver = attackData[4]
            otherId = getOtherId(playerId)
            if validCoord:
                socketio.emit('attackResult', (attackResult, coord), to=users[playerId])
                socketio.emit('defenceResult', (attackResult, coord), to=users[otherId])
            if gameOver:
                socketio.emit('gameVictory', to=users[playerId])
                socketio.emit('gameDefeat', to=users[otherId])
                # board.initialise()
            #if statement checking game over, if true broadcast victory page?


@socketio.on('removeBoatIfOnBoard')
def removeBoat(shipName):
    board = Board.instance()
    sid = request.sid
    playerId = users.index(sid)
    shipName = shipName.title()
    board.remove(shipName, playerId)

@socketio.on('clearBoard')
def clearBoard():
    board = Board.instance()
    sid = request.sid
    playerId = users.index(sid)
    board.clearBoard(playerId)
    board.printBoard(playerId)

@socketio.on('rotate')
def rotate(shipName):
    board = Board.instance()
    sid = request.sid
    playerId = users.index(sid)
    shipName = shipName.title()
    rotationValid, newOrientation = board.rotateShip(shipName, playerId)
    if rotationValid:
        board.printBoard(playerId)
        socketio.emit('rotate', newOrientation, to=users[playerId])

def getOtherId(playerId):
    if playerId == 0:
        otherId = 1
    else:
        otherId = 0
    return otherId


def initBoard():
    board = Board.instance()
    board.initialise()


if __name__ == "__main__":
    users = [None, None]
    initBoard()
    game = Game(Board.instance())
    print("Server has started!")
    socketio.run(server, port=5555)

