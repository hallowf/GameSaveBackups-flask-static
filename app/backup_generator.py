import os, pickle, shutil, zipfile
from Database.fetch_all_games import generate_games

tmp_path = "tmp_saves"

## Function to copy save files to tmp folder requires a list with dicts as parameter "games"
def copy_saves_toTmp(games):
    for game in games:
        if os.path.isdir(tmp_path + "/" + game["name"]):
            print("Removing old {} save files".format(game["name"]))
            shutil.rmtree(tmp_path + "/" + game["name"])
            print("Done")
        if os.path.isdir(game["path"]):
            print("Copying {} save files".format(game["name"]))
            shutil.copytree(game["path"], tmp_path + "/" + game["name"])
            print("Done")


## Function to make a zip archive # TODO: Replace shutil with a faster option,
## Add a index file with the paths for easier management
def make_zip_file():
    if os.path.isfile("ZippedBackups.zip"):
        print("Removig old zip")
        os.remove("ZippedBackups.zip")
        print("Done")
    if os.path.isdir(tmp_path):
        print("Making zip archive")
        shutil.make_archive("ZippedBackups", "zip", root_dir=tmp_path)
        print("Done, Removing tmp_files")
        shutil.rmtree(tmp_path)


def read_zip_file(filepath):
    slash = "/"
    zip_file = zipfile.ZipFile(filepath)
    path_list = zip_file.namelist()
    for x in path_list:
        print(x)
        x_str = str(x)
        if x_str.endswith(slash):
            str_find = x_str.split("/")[0]
            str_tuple = (str_find,)
    zip_file.close()

def delete_from_list(games):
    i = 0
    for game in games:
        if game["name"] == "Space Engineers":
            del games[i]
            print("lel")
        i = i + 1
    print(games)

#copy_saves_toTmp(generate_games())
#copy_saves_toTmp(pickle.load(open("games.pckl", "rb")))
#make_zip_file()
#read_zip_file()
#delete_from_list(pickle.load(open("games.pckl", "rb")))
