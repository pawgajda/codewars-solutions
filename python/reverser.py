# https://www.codewars.com/kata/58069e4cf3c13ef3a6000168
def reverse(n):
    rev = 0
    r = 0
    tmp = n
    
    while tmp > 0:
        r = tmp % 10
        rev = rev * 10 + r
        tmp = tmp // 10
        
    return rev
