# https://www.codewars.com/kata/53907ac3cd51b69f790006c5

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    # sort & unpack
    sides = sorted([a, b, c])
    a, b, c = sides
    # is it a triange?
    if a + b > c and a + c > b and b + c > a:
        # right
        if (a ** 2) + (b ** 2) == (c ** 2):
            return 2
        # acute
        elif (a ** 2) + (b ** 2) > (c ** 2):
            return 1
        # obtuse
        elif (a ** 2) + (b ** 2) < (c ** 2):
            return 3
    else:
        return 0
