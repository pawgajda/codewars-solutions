# https://www.codewars.com/kata/57a5c31ce298a7e6b7000334
#
# attempt #1:
def bin_to_decimal(inp):
    result = 0
    p = len(inp) - 1
    
    for i in inp:
        result += int(i) * 2 ** p
        p -= 1
    
    return result
#
# attempt #2:
def bin_to_decimal(inp):
    return int(inp, 2)
