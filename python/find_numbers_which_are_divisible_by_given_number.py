# https://www.codewars.com/kata/55edaba99da3a9c84000003b
def divisible_by(numbers, divisor):
    result = []
    
    for n in numbers:
        if n % divisor == 0:
            result.append(n)
            
    return result
