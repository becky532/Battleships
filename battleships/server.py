from flask_socketio import SocketIO, send
from flask import Flask, render_template

server = Flask(__name__)
server.config['SECRET_KEY'] = 'TeamTitanic'
socketio = SocketIO(server, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)



if __name__ == "__main__":
    socketio.run(server, allow_unsafe_werkzeug=True, port=5555)

