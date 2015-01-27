"""
Authors: Tron Team
Creation: December, 2014
Last update: 27.01.2015
Description: utility functions for the Tron Kart game
"""

import os

def get_file_names(path, pattern, t=1):
    """Get name of files/folders in a certain directory with a certain pattern.
        t represents the position in the file name where to search pattern:
            0 = if the file name starts with 'pattern';
            1 = if 'pattern' is at the end;
            2 = 'pattern' is in the name of the file"""
    file_names = [] # will hold eventually the files name (in path) that contain 'pattern'
    for file in os.listdir(path):
            if t == 0:
                if file.startswith(pattern):
                    file_names.append(file)
            if t == 1:
                if file.endswith(pattern):
                    file_names.append(file)
            if t == 2:
                if pattern in file:
                    file_names.append(file)
    return file_names
