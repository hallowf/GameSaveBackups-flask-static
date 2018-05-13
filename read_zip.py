import zipfile

def has_one_slash(filepath):
    return filepath.count('/') == 1

def read_zip_file(filepath):
    slash = '/'
    zip_file = zipfile.ZipFile(filepath)
    path_list = zip_file.namelist()
    path_list = filter(has_one_slash, path_list)
    new_list = list(path_list)
    print(new_list)
    zip_file.close()
    return new_list
