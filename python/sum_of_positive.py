# https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    # Your code here
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum
