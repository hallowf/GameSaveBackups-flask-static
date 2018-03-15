import os
import json
from classes import Game
import platform

save_database = json.load(open("database.json"))

def load_game(db_item):
    current_os = platform.system()
    path = ""
    [name, win_path, lin_path] = db_item
    if current_os == "Windows":
        path = win_path
        print(path)
    else:
        path = lin_path
        print(path)
    return Game(name, os.path.expanduser(path))

save_database = map(load_game, save_database)
