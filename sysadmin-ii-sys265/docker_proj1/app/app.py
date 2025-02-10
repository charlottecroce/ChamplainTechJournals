from flask import Flask, render_template
from flask_socketio import SocketIO, send

# initialize flask and socketio
app = Flask(__name__)
socketio = SocketIO(app)

# default page
@app.route('/')
def index():
    return render_template('index.html')

# runs when message is received on socket
@socketio.on('message')
def handle_message(msg):
    print("message: " + msg)
    send(msg, broadcast=True)

# open websocket, listen on port 5000
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
