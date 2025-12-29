# https://www.codewars.com/kata/5250a89b1625e5decd000413
#
# attempt #1:
def flatten(lst):
    result = []

    for i in lst:
        if type(i) in (list, tuple):
            for j in i:
                result.append(j)
        else:
            result.append(i)
            
    return result
#
# attempt #2:
def flatten(lst):
    result = []
    
    for i in lst:
        if type(i) in (list, tuple):
            result.extend(i)
        else:
            result.append(i)
            
    return result
