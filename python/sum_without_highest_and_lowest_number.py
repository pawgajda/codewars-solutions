# https://www.codewars.com/kata/576b93db1129fcf2200001e6
def sum_array(arr):
    if arr is None:
        return 0
    elif len(arr) <= 2:
        return 0
    
    # remove min & max values
    arr.pop(arr.index(min(arr)))
    arr.pop(arr.index(max(arr)))
    
    return sum(arr)
