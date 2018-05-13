import platform
import os
current_os = platform.system()
from Database import database
from steam_id import convert_id
if current_os == "Windows":
    import win32api
else:
    current_os = "Linux"

def convert_path(user_id):
    if current_os == "Windows":
        for game in database.save_database:
            new_sync = game.sync_path.replace("XXXXX", str(user_id))
            drive_letters = win32api.GetLogicalDriveStrings().split("\000")[:-1]
            for drive in drive_letters:
                new_path = new_sync.replace("C:\\", drive)
                if os.path.isdir(new_path):
                    game.sync_path = new_path
                    yield game.to_dict()
                else:
                    print("Couldn't find " + game.name + " at " + new_path)
    else:
        for game in database.save_database:
            new_sync = game.sync_path.replace("XXXXX", str(user_id))
            if os.path.isdir(new_sync):
                yield game.to_dict()
            else:
                print ("Couldn't find " + game.name + " at " + new_sync)
