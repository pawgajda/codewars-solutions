# https://www.codewars.com/kata/5413759479ba273f8100003d
def reverse(lst):
    result = list()
    
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
        
    return result
