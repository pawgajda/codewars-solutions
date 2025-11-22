# https://www.codewars.com/kata/564d398e2ecf66cec00000a9
def type_of_triangle(a, b, c): 
    # check types
    if all([isinstance(n, int) for n in (a, b, c)]) is False:
        return "Not a valid triangle"
    
    # check if is a valid triangle
    if a < b + c and b < a + c and c < b + a:
        # all sides of equal length
        if a == b == c:
            return "Equilateral"
        # two sides of equal length
        elif a == b or a == c or b == c:
            return "Isosceles"
        # all sides of different length
        else:
            return "Scalene"
    else:
        return "Not a valid triangle"
