# https://www.codewars.com/kata/584ebd7a044a1520f20000d5
#
# attempt #1:
def range_function(*args):
    result = []

    if len(args) == 1:
        i = 1
        while i <= args[0]:
            result.append(i)
            i += 1
    
    elif len(args) == 2:
        i = args[0]
        while i <= args[1]:
            result.append(i)
            i += 1
    
    elif len(args) == 3:
        i = args[0]
        
        while i <= args[2]:
            result.append(i)
            i += args[1]
            
    return result
#
# attempt #2:
def range_function(*args):
    match len(args):
        case 1:
            start, step, stop = 1, 1, args[0]
        case 2:
            start, step, stop = args[0], 1, args[1]
        case 3:
            start, step, stop = args[0], args[1], args[2]
    
    result = []

    while start <= stop:
        result.append(start)
        start += step
        
    return result
#
# attempt #3:
def range_function(*args):
    match len(args):
        case 1:
            start, step, stop = 1, 1, args[0]
        case 2:
            start, step, stop = args[0], 1, args[1]
        case 3:
            start, step, stop = args[0], args[1], args[2]

    while start <= stop:
        yield start
        start += step
