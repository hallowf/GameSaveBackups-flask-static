import os
import win32api
from Database import database

def find_game ():
    for game in database.save_database:
        drive_letters = win32api.GetLogicalDriveStrings().split("\000")[:-1]
        for drive in drive_letters:
            new_path = game.path.replace("C:\\", drive)
            if os.path.isdir(new_path):
                game.path = new_path
                yield game.to_dict()
            else:
                print("Couldn't find " + new_path)
