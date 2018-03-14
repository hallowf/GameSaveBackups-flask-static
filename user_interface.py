import savebackup
from database import save_database
import eel
import platform
from search_disks import find_game


@eel.expose
def search_all_disks():
    current_os = platform.system()
    if current_os == "Windows":
        all_games = list(find_game())
        print (all_games)
        return all_games
    else:
        games_list = list(savebackup.check_game())
        print(games_list)
        return games_list
#@eel.expose
#def get_games():
#    games_list = list(savebackup.check_game())
#    print(games_list)
#    return games_list

@eel.expose
def make_backup(game):
    try:
        savebackup.make_backup(game)
    except:
        print ("game already exists")

@eel.expose
def make_zip():
    savebackup.make_zip()


eel.init("web")
eel.start("index.html")
