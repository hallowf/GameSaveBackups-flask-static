import os
import json
from . import classes
import platform

save_database = json.load(open("Database\\database.json"))

def load_game(db_item):
    current_os = platform.system()
    path = ""
    sync_path = ""
    [name, win_path, win_sync, lin_path, lin_sync] = db_item
    if current_os == "Windows":
        sync_path = win_sync
        path = win_path
        print(path, sync_path)
    else:
        sync_path = lin_sync
        path = lin_path
        print(path, sync_path)
    print(classes.Game(name, os.path.expanduser(path), os.path.expanduser(sync_path)))
    return classes.Game(name, os.path.expanduser(path), os.path.expanduser(sync_path))

save_database = list(map(load_game, save_database))