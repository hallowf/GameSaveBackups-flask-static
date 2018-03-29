import savebackup
from database import save_database
import eel
import platform
import search_sync_path
import steam_id

if platform.system() == "Windows":
    import search_disks
    search_disks.find_game()
else:
    print ("Linux detected")

@eel.expose
def convert_into_ID3(user_id):
    steam_id3 = steam_id.convert_id(user_id)
    return steam_id3


@eel.expose
def get_steam_sync(user_id):
    sync_paths = list(search_sync_path.convert_path(user_id))
    return sync_paths


@eel.expose
def search_all_disks():
    current_os = platform.system()
    if current_os == "Windows":
        all_games = list(search_disks.find_game())
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
