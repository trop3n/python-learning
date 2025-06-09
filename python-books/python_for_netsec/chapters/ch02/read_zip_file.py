import zipfile
def list_files_in_zip(filename):
    with zipfile.Zipfile(filename) as myzip:
        for zipinfo in myzip.infolist():
            yield zipinfo.filename
for filename in list_files_in_zip("files.zip"):
    print(filename)