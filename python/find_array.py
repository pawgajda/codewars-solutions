# https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055
def find_array(arr1, arr2):
    result = []
    
    for i in arr2:
        if i <= (len(arr1) - 1):
            result.append(arr1[i])
    
    return result
