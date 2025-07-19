# https://www.codewars.com/kata/52f3149496de55aded000410
def sum_digits(number):
    return sum([int(num) for num in str(number) if num is not "-" ])
