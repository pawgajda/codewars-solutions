# https://www.codewars.com/kata/524f5125ad9c12894e00003f
def remainder(a,b):
    try:
        return max(a, b) % min (a, b)
    except ZeroDivisionError:
        return None
