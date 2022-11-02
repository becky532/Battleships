from flask_socketio import SocketIO, send
from flask import Flask, render_template
from gameBack import board

server = Flask(__name__)
server.config['SECRET_KEY'] = 'TeamTitanic'
socketio = SocketIO(server, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
    print(msg)
    # gameback function
    send(msg, broadcast=True) #player 2 sent (coord, if hit)

    # can we return data to player 1?

if __name__ == "__main__":
    socketio.run(server, allow_unsafe_werkzeug=True, port=5555)

