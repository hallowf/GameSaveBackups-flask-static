from flask_socketio import SocketIO, emit
from app import socketio
from app.Database.fetch_all_games import generate_games, convert_path

#### # FIXME: This should be in socket_events but if imported that way monkey patch produces a # BUG: https://github.com/gevent/gevent/issues/1016
### Socket events
@socketio.on("event listener", namespace="/websocket")
def test_message(message):
    emit("response", {"data": message["data"]})

@socketio.on("data request", namespace="/websocket")
def send_data(message):
    print(message["request"][:13])
    if message["request"] == "search_unsynced":
        emit("unsynced_game_list", {"dict": generate_games()})
    elif message["request"][:13] == "search_synced":
        user_id = message["request"].replace("search_synced ", "")
        emit("synced_game_list", {"dict": convert_path(user_id)})

@socketio.on("broadcast event", namespace="/websocket")
def test_message(message):
    emit("response", {"data": message["data"]}, broadcast=True)

@socketio.on("connect", namespace="/websocket")
def test_connect():
    emit("response", {"data": "Connected"})

@socketio.on("disconnect", namespace="/websocket")
def test_disconnect():
    print("Client disconnected")
