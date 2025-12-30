# https://www.codewars.com/kata/5810085c533d69f4980001cf
def calculator(x, y, op):
    if type(x) not in (int, float) or type(y) not in (int, float):
        return "unknown value"

    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y
        case _:
            return "unknown value"
