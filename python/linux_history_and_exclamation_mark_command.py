# https://www.codewars.com/kata/58143221f9588e340e00009f
def bang_bang(history):
    # convert history string to list by splitting and newline character
    hislist = history.split("/n")
    # assume that the last list element is the last cmd string
    # turn the last cmd string into list by splitting at "  " (two spaces)
    # return the last string of the list as string
    last_cmd = hislist[-1].split("  ")[-1]
    return last_cmd
