import tempfile
import os
import zipfile
import shutil
from database import save_database
from read_zip import read_zip_file

tmp_dir = tempfile.mkdtemp()
tmp_filename = ""

tmp_path = os.path.join(tmp_dir, tmp_filename)

def check_game():
    for game_exists in save_database:
        if os.path.isdir(game_exists.path):
            yield game_exists.to_dict()
        else:
            print ("could not find ", game_exists.name)


def make_backup(game):
    if os.path.isdir(os.path.join(tmp_path + game["name"])):
        print ("Removing old tmp files")
        os.rmdir(tmp_path + game["name"])
        print ("Removed old tmp files")
    else:
        print ("No need to remove old temp files")
    try:
        print ("Making new tmp files")
        shutil.copytree(game["path"], tmp_path + game["name"],)
        print("Made tmp files")
    except:
        print ("can't make tmp files")


def make_zip():
    if os.path.isfile("zippedBackups.zip"):
        print ("Checking games")
        #read_zip_file()
        os.remove("zippedBackups.zip")
        print ("Done")
    else:
        print ("No need to remove old backups")
    if os.path.isdir(tmp_path):
        print("Making zip archive")
        shutil.make_archive("zippedBackups", "zip", root_dir=tmp_path)
        print("Done")
    else:
        print ("can't make archive")

def add_to_zip(game, z_file):
    if os.path.isfile(z_file):
        print("Checking games")
        saves_list = list(set(read_zip_file(z_file)))
        print(saves_list)
        if game in saves_list:
            print("Your save already exists")
        else:
            print("Adding game")
            z = zipfile.ZipFile(z_file, "a")
            z.write(game)
            z.close





add_to_zip("Game", "zippedBackups.zip")
