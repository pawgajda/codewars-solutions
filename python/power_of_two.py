# https://www.codewars.com/kata/534d0a229345375d520006a0
def power_of_two(x):
    if x == 0:
        return False
    
    return x & (x - 1) == 0
