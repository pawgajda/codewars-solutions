# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
def multi_table(number):
    result = []
    for i in range (1, 11):
        result.append(f"{i} * {number} = {i * number}")
    return "\n".join(result)
