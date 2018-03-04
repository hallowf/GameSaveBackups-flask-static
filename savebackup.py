import tempfile
import os
import zipfile
import shutil
from database import save_database

tmp_dir = tempfile.mkdtemp()
tmp_filename = ""

tmp_umask = os.umask(0077)

tmp_path = os.path.join(tmp_dir, tmp_filename)

def check_game():
    for game_exists in save_database:
        if os.path.isdir(game_exists.path):
            yield game_exists.to_dict()
        else:
            print ("could not find ", game_exists.name)


def make_backup (search):
    try:
        shutil.copytree(search["path"], tmp_path + search["name"],)
    except:
        print ("can't make temp files")


def make_zip ():
    try:
        shutil.make_archive("zippedBackups", "zip", root_dir=".", base_dir=tmp_path)
    except:
        print ("can't make archive")
        #shutil.make_archive("R:\\backzips", "zip", "R:\\backs\\")
        #shutil.rmtree("R:\\backs")




#def make_backup ():

    # remove old unzipped folder
#    try:
#        shutil.rmtree("R:\\backs")
#    except:
#        pass
#    # remove old zipped folder
#    try:
#        os.remove("R:\\backzips.zip")
#    except:
#        pass

    # check if game exists then make backups
#    for game_exists in save_database:
#        if os.path.isdir(game_exists.path):
#            shutil.copytree(game_exists.path, "R:\\backs\\" + game_exists.name,)
#        else:
#            print (game_exists.name, "could not be found")


#    for game_exists in save_database:
#        try:
#            shutil.copytree(game_exists.path,"R:\\backs\\" + game_exists.name,)
#        except:
#            print (game_exists.name, "could not be found")

    # creates zipped archive
#    shutil.make_archive("R:\\backzips", "zip", "R:\\backs\\")

    # removes unzipped folder
#    try:
#        shutil.rmtree("R:\\backs")
#    except:
#        pass
