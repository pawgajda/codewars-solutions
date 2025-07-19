# https://www.codewars.com/kata/5822b65bb81f702016000026
def linux_type(file_attribute):
    # create a map of filetypes
    filetypes = {
        "-": "file",
        "d": "directory",
        "l": "symlink",
        "c": "character_file",
        "b": "block_file",
        "p": "pipe",
        "s": "socket",
        "D": "door"
    }
    
    # assume the character with index is the filetype and
    # use it as a key for filetypes dictionary
    return filetypes[file_attribute[0]]
