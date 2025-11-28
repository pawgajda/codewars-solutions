# https://www.codewars.com/kata/564fa92d1639fbefae00009d
def factors(x):
    if type(x) is not int or x <= 0:
        return -1
    else:
        result = []
        for i in range(x, 0, -1):
            if x % i == 0:
                result.append(i)
        return result
