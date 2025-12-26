# https://www.codewars.com/kata/57b71a89b69bfc92c7000170
#
# attempt #1:
def get_number_of_squares(n):
    result = 0 
    
    for i, num in enumerate(range(1, n + 1)):
        if result < n:
            result += num ** 2
        else:
            return i - 1
    return i
#
# attempt #2:
def get_number_of_squares(n):
    count, result = 0, 0
    num = 1
    
    while result < n:
        result += num ** 2
        num += 1
        count += 1
        
    return count - 1

