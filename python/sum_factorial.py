# https://www.codewars.com/kata/56b0f6243196b9d42d000034
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n - 1)

def sum_factorial(lst):
    return sum([factorial(x) for x in lst])

