import os
import zipfile
import shutil
from database import save_database

def make_backup ():
    try:
        os.remove("R:\\backzips.zip")
    except:
        pass


    for game_exists in save_database:
        try:
            shutil.copytree(game_exists.path,"R:\\backs\\" + game_exists.name,)
        except:
            print (game_exists.name, "could not be found")

    shutil.make_archive("R:\\backzips", "zip", "R:\\backs\\")

    try:
        shutil.rmtree("R:\\backs")
    except:
        pass
