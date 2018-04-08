import zipfile
from read_zip import read_zip_file
from database import save_database
from database import load_game


def add_to_zip(zfile, sfile):
    z_file = zipfile.ZipFile(zfile, "a")
    z_file.write(sfile)
    z_file.close()



def append_to_zip(zfile, sfile):
    #Append the files to zip






def try_reading():
    for game in save_database:
        game_name = ""
        game_dict = game.to_dict()
        if "name" in game_dict:
            game_name = game_dict["name"]
            print(game_name)
