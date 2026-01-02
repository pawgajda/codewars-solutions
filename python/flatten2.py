# https://www.codewars.com/kata/513fa1d75e4297ba38000003
def flatten(*args) -> list:
    result = []
    
    for arg in args:
        if type(arg) in (list, tuple):
            # recursively unpack the list/tuple by using .extend()
            # pass it as *arg instead of arg to get '(1, 2)'
            # to iterate over instead of '([1, 2],)'
            result.extend(flatten(*arg))
        else:
            result.append(arg)
 
    return result
