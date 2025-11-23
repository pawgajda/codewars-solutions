# https://www.codewars.com/kata/59a96d71dbe3b06c0200009c
def generate_shape(n):
    result = ""
    # draw a square
    for i in range(n):
        result += "+" * n
        # range(n) up to n - 1
        if i < (n - 1):
            result += "\n"
    return result
