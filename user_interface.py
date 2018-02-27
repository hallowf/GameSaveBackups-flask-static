import savebackup
from database import save_database
import eel

@eel.expose
def get_games():
    print(list(savebackup.check_game()))
    return list(savebackup.check_game())

@eel.expose
def call_backup():
    savebackup.make_backup()
eel.init("web")
eel.start("index.html")
