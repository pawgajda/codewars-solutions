# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
def sort_array(source_array):
    arr = source_array.copy()
    n = len(arr)
    
    # iterate through all list elements
    for i in range(n):
        # iterate from i until the end
        for j in range(i, n):
            # if arr[i] && arr[j] are odd
            if arr[i] % 2 != 0 and arr[j] % 2 != 0:
                # compare and swap if arr[i] > arr[j]
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr
