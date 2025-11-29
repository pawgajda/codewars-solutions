# https://www.codewars.com/kata/57bf599f102a39bb1e000ae5
from functools import cache


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


def fibs_fizz_buzz(n):
    fib = [fibonacci(n) for n in range(1, n + 1)]
    fizz = [fizzbuzz(n) for n in fib]
    return fizz
