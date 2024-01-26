# os module
# path info
# honestly https://docs.python.org/3/library/os.path.html
# is good

import os

# get full absolute path to this location, these are equal
os.path.abspath(path)
os.path.normpath(os.path.join(os.getcwd(), path))

os.path.exists(path)

os.path.isfile(path)

os.path.join(path, *paths)