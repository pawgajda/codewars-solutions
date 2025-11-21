# https://www.codewars.com/kata/562926c855ca9fdc4800005b
def number_to_pwr(number, p): 
    # your code here
    n = 1
    i = 0
    
    while i < p:
        n *= number
        i += 1
        
    return n
