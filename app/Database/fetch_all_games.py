import os
import json
import platform
from app.utilities.id_converter import convert_id

### Check OS
current_os = platform.system()

if current_os.upper() == "WINDOWS":
    import win32api
else:
    pass


### class for constructing game objects

class Game():
    def __init__(self, game_name, game_path, sync_path):
        self.name = game_name
        self.path = game_path
        self.sync_path = sync_path
        self.found = False
    def to_dict(self):
        self.name
        self.path
        self.sync_path
        return {"name": self.name, "path": self.path, "sync_path": self.sync_path, "found": self.found}


### The game database to load
save_database = json.load(open("app/Database/database.json"))

#save_database = json.load(open("database.json"))


### Function to return game objects
def load_game(db_item):
    current_os = platform.system()
    path = ""
    sync_path = ""
    [name, win_path, win_sync, lin_path, lin_sync] = db_item
    if current_os == "Windows":
        sync_path = win_sync
        path = win_path
    else:
        sync_path = lin_sync
        path = lin_path
    return Game(name, os.path.expanduser(path), os.path.expanduser(sync_path))


### Assign to save_database a list with each game and it's attributes from the database
save_database = list(map(load_game, save_database))



### Functions to yield games to dict

## Simple function that returns all games
## Wont work for steam sync
def generate_games():
    g = []
    for game in save_database:
        if os.path.isdir(game.path) and game.found == False:
            g.append(game.to_dict())
            game.found = True
        else:
            continue
    return g



### Check the OS and searches for the games in steam library's across all hard drives
## TODO: At the moment it can only search all drives in windows, add linux functionality
def convert_path(user_id):
    user_id = convert_id(user_id)
    g = []
    if current_os == "Windows":
        drive_letters = win32api.GetLogicalDriveStrings().split("\000")[:-1]
        for game in save_database:
            new_sync = game.sync_path.replace("XXXXX", str(user_id))
            for drive in drive_letters:
                if os.path.isdir(new_sync) and game.found == False:
                    game.sync_path = new_sync
                    print("Found " + game.name + " at " + game.sync_path)
                    game.found = True
                    g.append(game.to_dict())
                else:
                    new_path = new_sync.replace("C:\\", drive)
                    if os.path.isdir(new_path) and game.found == False:
                        print("Found " + game.name + " at " + new_path)
                        game.found = True
                        game.sync_path = new_path
                        g.append(game.to_dict())
                    elif os.path.isdir(new_path) == False and game.found == False:
                        print("Couldn't find " + game.name + " at " + new_path)
        return g
    else:
        for game in save_database:
            new_sync = game.sync_path.replace("XXXXX", str(user_id))
            if os.path.isdir(new_sync) and game.found == False:
                print("Found game at:" + new_sync)
                game.found = True
                g.append(game.to_dict())
            elif os.path.isdir(new_sync) == False and game.found == False:
                print ("Couldn't find " + game.name + " at " + new_sync)
        return g
