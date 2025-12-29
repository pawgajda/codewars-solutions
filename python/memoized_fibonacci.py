# https://www.codewars.com/kata/529adbf7533b761c560004e5
#
# attempt #1:
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
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
#
# attempt #2:
def memoize(func):
    cache = {}
    
    def wrapper(key):
        if key not in cache:
            cache[key] = func(key)
        return cache[key]

    return wrapper


@memoize
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
