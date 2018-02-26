import json
from classes import Game

save_database = json.load(open("database.json"))

def load_game(db_item):
    [name, path] = db_item
    return Game(name, path)

save_database = map(load_game, save_database)
