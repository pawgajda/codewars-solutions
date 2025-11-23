# https://www.codewars.com/kata/544d114f84e41094a9000439
def perfect_square(n):
    x = n ** 0.5
    return x*x == n


def powerof2(n):
    return n & (n - 1) == 0


def powerof4(n):
    # check types
    if type(n) is not int:
        return False

    if n == 0:
        return False
    
    # check if n is a perfect square and a power of two
    return perfect_square(n) and powerof2(n)
