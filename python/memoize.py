# https://www.codewars.com/kata/59ffef8246d8434b0700001d
#
# attempt #1:
from preloaded import count_calls
from functools import wraps


def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(key):
        if key not in cache:
            cache[key] = func(key)
        return cache[key]

    return wrapper


@memoize
def fib(n):
    """Computes the nth number in the Fibonacci sequence"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
#
# attempt #2:
from preloaded import count_calls


def memoize(func):
    cache = {}
    
    def wrapper(key):
        if key not in cache:
            cache[key] = func(key)
        return cache[key]

    # preserve function name and doc
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


@memoize
def fib(n):
    """Computes the nth number in the Fibonacci sequence"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
