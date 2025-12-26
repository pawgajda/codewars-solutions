# https://www.codewars.com/kata/58fa273ca6d84c158e000052
#
# attempt #1:
def digits(n):
    digits = 0
    
    if n == 0:
        return 1

    while n > 0:
        n = n // 10
        digits += 1
        
    return digits
#
# attempt #2:
def digits(n):
    return len(str(n))
