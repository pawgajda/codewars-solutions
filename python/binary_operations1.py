# https://www.codewars.com/kata/560e80734267381a270000a2
def flip_bit(value, bit_index):
    return value ^ (1 << bit_index - 1)
