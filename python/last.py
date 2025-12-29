# https://www.codewars.com/kata/541629460b198da04e000bb9
#
# attempt #1:
def last(*args):
    
    if len(args) == 1 and type(args[0]) in (str, list, tuple):
        return args[0][-1]
    else:
        parsed_args = [arg for arg in args]
        return parsed_args[-1]
#
# attempt #2:
def last(*args):
    
    if len(args) == 1:
        if type(args[0]) in (str, list, tuple):
            return args[0][-1]
        else:
            return args[0]
    else:
        return [arg for arg in args][-1]
