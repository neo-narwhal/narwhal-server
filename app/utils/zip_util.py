import zipfile
import os


def unzip(path):
    with zipfile.ZipFile(path, 'r') as zf:
        print(path)
        zf.extractall(os.path.dirname(path))
    os.remove(path)
