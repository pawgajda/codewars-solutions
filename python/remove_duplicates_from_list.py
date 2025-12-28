# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
def distinct(seq):
    result = []
    
    for i in seq:
        if i not in result:
            result.append(i)
            
    return result
