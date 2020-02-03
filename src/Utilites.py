import os

def get_filename(relpath):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, relpath)