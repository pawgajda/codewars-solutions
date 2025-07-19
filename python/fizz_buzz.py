# https://www.codewars.com/kata/51dda84f91f5b5608b0004cc
def solution(number):
    result = {"fizz": 0, "buzz": 0, "fizzbuzz": 0}
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            result["fizzbuzz"] += 1
        elif i % 3 == 0:
            result["fizz"] += 1
        elif i % 5 == 0:
            result["buzz"] += 1
    return [result["fizz"], result["buzz"], result["fizzbuzz"]]
