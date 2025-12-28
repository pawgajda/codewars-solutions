# https://www.codewars.com/kata/57fb04649610ce369a0006b8
#
# attempt #1:
def remove(s):
    result = []
    for w in s.split():
        # equal number of '!'
        if len(w.lstrip("!")) == len(w.rstrip("!")):
            result.append(w)
        # more '!' on the left
        elif len(w.lstrip("!")) < len(w.rstrip("!")):
            result.append(w[len(w.rstrip("!")) - len(w.lstrip("!")):])
        # more '!' on the right
        elif len(w.lstrip("!")) > len(w.rstrip("!")):
            result.append(w[:len(w) - len(w.lstrip("!")) + len(w.rstrip("!"))])
            
    return " ".join(result)
#
# attempt #2:
def remove(s):
    result = []

    for w in s.split():
        left = len(w) - len(w.lstrip("!"))
        right = len(w) - len(w.rstrip("!"))
        
        result.append((min(left, right) * "!" + w.strip("!") + min(left, right) * "!"))
        
    return " ".join(result)
