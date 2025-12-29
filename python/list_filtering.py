# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    result = []

    for i in l:
        if type(i) is int:
            result.append(i)
            
    return result
