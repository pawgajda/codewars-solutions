# https://www.codewars.com/kata/57efcb78e77282f4790003d8
#
# attempt #1
def how_many_times(annual_price, individual_price):
    if annual_price % individual_price != 0:
        return (annual_price // individual_price) + 1
    else:
        return annual_price // individual_price
#
# attempt #2:
from math import ceil


def how_many_times(annual_price, individual_price):
    return ceil(annual_price / individual_price)
