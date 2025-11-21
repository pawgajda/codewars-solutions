# https://www.codewars.com/kata/53daa9e5af55c184db00025f
def is_prime(n):
    'Return True if n is a prime number otherwise return False'
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
