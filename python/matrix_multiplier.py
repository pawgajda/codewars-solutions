# https://www.codewars.com/kata/573248f48e531896770001f9
def get_matrix_product(a, b):
    # rows(a) * columns(b) when columns(a) == rows(b)
    if len(a[0]) == len(b):
        # initialize empty reuslt list
        result = []
        # i - row of a
        for i in range(0, len(a)):
            # initialize empty row result[[]]
            result.append([])
            # j - column of b
            for j in range(0, len(b[0])):
                # initialize empty column result[[0]]
                result[i].append(0)
                # k = common (rows of a, columns of b)
                for k in range(0, len(b)):
                    # a[i][k] * b[k][j]
                    result[i][j] += a[i][k] * b[k][j]
        return result
    else:
        return None
