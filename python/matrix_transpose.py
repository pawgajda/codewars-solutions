# https://www.codewars.com/kata/52fba2a9adcd10b34300094c
def transpose(matrix):
    result = []

    if len(matrix) >= 0 and len(matrix[0]) >= 0:
        # columns of matrix
        for i in range(0, len(matrix[0])):
            # create empty row in result matrix
            result.append([])
            # rows of matrix
            for j in range(0, len(matrix)):
                # append value of column to row
                result[i].append(matrix[j][i])
                
    return result
