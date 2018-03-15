import zipfile

def read_zip_file(filepath):
    zip_file = zipfile.ZipFile(filepath)
    print (zip_file.namelist())
    zip_file.close()
        
