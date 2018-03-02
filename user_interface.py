import savebackup
from database import save_database
import eel

@eel.expose
def get_games():
    games_list = list(savebackup.check_game())
    print(games_list)
    return games_list

@eel.expose
def make_backup(search):
    try:
        savebackup.make_backup(search)
    except:
        print ("game already exists")

@eel.expose
def make_zip():
    savebackup.make_zip()


eel.init("web")
eel.start("index.html")
