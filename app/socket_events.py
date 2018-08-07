from flask_socketio import SocketIO, emit
from app import socketio

### Socket events
@socketio.on("event listener", namespace="/websocket")
def test_message(message):
    print(message["data"])
    emit("my response", {"data": message["data"]})

@socketio.on("broadcast event", namespace="/websocket")
def test_message(message):
    emit("my response", {"data": message["data"]}, broadcast=True)

@socketio.on("connect", namespace="/websocket")
def test_connect():
    emit("my response", {"data": "Connected"})

@socketio.on("disconnect", namespace="/websocket")
def test_disconnect():
    print("Client disconnected")
