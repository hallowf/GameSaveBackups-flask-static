from flask_socketio import SocketIO, emit
from app import app


### App parameters
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


### Socket events
@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')





# Run app

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1",port=2890, debug=True)
