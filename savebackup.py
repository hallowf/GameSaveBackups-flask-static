import tempfile
import os
import zipfile
import shutil
from database import save_database
import read_zip

tmp_dir = tempfile.mkdtemp()
tmp_filename = ""

#tmp_umask = os.umask(0077)

tmp_path = os.path.join(tmp_dir, tmp_filename)

def check_game():
    for game_exists in save_database:
        if os.path.isdir(game_exists.path):
            yield game_exists.to_dict()
        else:
            print ("could not find ", game_exists.name)


def make_backup (game):
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


def make_zip ():
    if os.path.isfile("zippedBackups.zip"):
        #zip_file = read_zip.read_zip_file()
        print ("Checking games")
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
