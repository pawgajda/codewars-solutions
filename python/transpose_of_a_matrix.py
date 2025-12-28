# https://www.codewars.com/kata/559656796d8fb52e17000003
def transpose(arr):
    result = []
    
    if len(arr) >= 0 and len(arr[0]) >= 0:
        # columns of matrix
        for i in range(0, len(arr[0])):
            # create empty row in result matrix
            result.append([])
            # rows of matrix
            for j in range(0, len(arr)):
                # append value of column to row
                result[i].append(arr[j][i])

    return result
