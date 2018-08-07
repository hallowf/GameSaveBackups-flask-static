import os
import json
import platform


### class for constructing game objects

class Game():
    def __init__(self, game_name, game_path, sync_path):
        self.name = game_name
        self.path = game_path
        self.sync_path = sync_path
    def to_dict(self):
        self.name
        self.path
        self.sync_path
        return {"name": self.name, "path": self.path, "sync_path": self.sync_path}




### The game database to load
save_database = json.load(open("app\\Database\\database.json"))




### Function to return game objects
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

## Assign to save_database a list with each game and it's attributes from the database

save_database = list(map(load_game, save_database))

def generate_games():
    g = []
    for game in save_database:
        g.append(game.to_dict())
    return g
