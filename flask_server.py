import eventlet
eventlet.monkey_patch()
import os
from app import app, socketio


### App parameters
app.config['SECRET_KEY'] = 'secret!'



# Run app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "2890"))
    socketio.run(app, host="0.0.0.0",port=port, debug=True)
