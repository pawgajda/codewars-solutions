# https://www.codewars.com/kata/53e248c9af0d91a45b000e71
#
# attempt #1:
from os import mkdir
import os.path

def mkdirp(*directories):
    """Recursively create all directories as necessary"""
    path = os.path.join(*directories)
    parent = os.path.dirname(path)
    
    # directory does not exist
    if not os.path.exists(path):
        # parent directory aleady exists
        if os.path.exists(parent):
            mkdir(path)
        # parent directory does not exist - recursive call
        else:
            mkdirp(parent)
            mkdir(path)
#
# attempt #2:
from os import mkdir
import os.path

def mkdirp(*directories):
    """Recursively create all directories as necessary"""
    path = os.path.join(*directories)

    # directory does not exist    
    if not os.path.exists(path):
        parent = os.path.dirname(path)
        
        # create parent directory recursively if it does not exist 
        if not os.path.exists(parent):
            mkdirp(parent)

        # create the directory after ensuring that parent parent directory exists   
        mkdir(path)
