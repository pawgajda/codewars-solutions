# https://www.codewars.com/kata/57fafb6d2b5314c839000195
def remove(s):
    result = []
    
    for w in s.split():
        if w.count("!") != 1:
            result.append(w)
    
    return " ".join(result)
