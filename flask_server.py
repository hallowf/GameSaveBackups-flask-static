import eventlet
eventlet.monkey_patch()
from app import app, socketio


### App parameters
app.config['SECRET_KEY'] = 'secret!'


# Run app

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1",port=2890, debug=True)
