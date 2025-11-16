# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
def factorial(n):
    # handle invalid inputs
    if n < 0 or n > 12:
        raise ValueError
    else:
        # iterative implementation of factorial
        factorial = 1
        i = 1

        while i <= n:
            factorial *= i
            i += 1

        return factorial

