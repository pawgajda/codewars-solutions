# https://www.codewars.com/kata/56b97b776ffcea598a0006f2
def bubblesort_once(l):
    # initialize new list
    arr = l.copy()
    
    # this is an "inner" loop of normal BubbleSort
    # traverse through len(arr) - 1 because it's just single pass
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            # swap elements
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr
