import zipfile, os

def has_one_slash(filepath):
    return filepath.count("/") == 1

def read_zip_file(filepath):
    slash = "/"
    zip_file = zipfile.ZipFile(filepath)
    path_list = zip_file.namelist()
    for x in path_list:
        x_str = str(x)
        if x_str.endswith(slash):
            str_find = x_str.split("/")[0]
            str_tuple = (str_find,)
            yield str_find
    zip_file.close()


def read_tmp_path(folderpath):
    sub_folders = os.listdir(folderpath)
    return sub_folders
