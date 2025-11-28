# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
def is_square(n):
    if n >= 0:
        sqrt = n ** 0.5
        return sqrt * sqrt == n
    return False
