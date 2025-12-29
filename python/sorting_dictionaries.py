# https://www.codewars.com/kata/53da6a7e112bd15cbc000012
#
# attempt #1:
from operator import itemgetter

def sort_dict(d):
    result = []
    for k, v in d.items():
        result.append((k, v))
        
    result.sort(key=itemgetter(1), reverse=True)
    return result
#
# attempt #2:
from operator import itemgetter

def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1), reverse=True)
