import platform
import os
current_os = platform.system()
from database import save_database
from steam_id import convert_id
if current_os == "Windows":
    import win32api
else:
    current_os = "Linux"

def convert_path(user_id):
    for game in save_database:
        new_sync = game.sync_path.replace("XXXXX", str(user_id))
        game.sync_path = new_sync
        if current_os == "Windows":
            drive_letters = win32api.GetLogicalDriveStrings().split("\000")[:-1]
            for drive in drive_letters:
                new_path = game.sync_path.replace("C:\\", drive)
                if os.path.isdir(new_path):
                    game.sync_path = new_path
                    yield game.to_dict()
                else:
                    print("Couldn't find " + new_path)
        else:
            for game_exists in save_database:
                if os.path.isdir(game_exists.sync_path):
                    yield game_exists.to_dict()
                else:
                    print ("could not find ", game_exists.name)
