import zipfile


def add_to_zip(zfile, game):
    z_file = zipfile.ZipFile(zfile, "a")
    z_file.write(game)
    z_file.close()
    z_file = zipfile.ZipFile(zfile)
    z_file.printdir()



add_to_zip("zippedBackups.zip", "Game")
