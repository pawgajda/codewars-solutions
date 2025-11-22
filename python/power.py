# https://www.codewars.com/kata/562926c855ca9fdc4800005b


# attempt 1:
def number_to_pwr(number, p): 
    # your code here
    if p == 0:
        return 1
    else:
        n = number
        i = 1
        while i < p:
            n *= number
            i += 1
        return n


# attempt 2:
def number_to_pwr(number, p): 
    # your code here
    n = 1
    i = 0
    
    while i < p:
        n *= number
        i += 1
        
    return n


# attempt 3:
def number_to_pwr(number, p): 
    # your code here
    n = 1
    
    for _ in range(p):
        n *= number
    return n
