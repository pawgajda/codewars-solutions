# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
#
# attempt #1:
def binary_array_to_number(arr):
    return int("".join(str(x) for x in arr), 2)
#
# attempt #2:
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
#
# attempt #3:
def binary_array_to_number(arr):
    return sum([v * 2 ** i for i, v in enumerate(reversed(arr))])
