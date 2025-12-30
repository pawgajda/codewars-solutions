# https://www.codewars.com/kata/546ba103f0cf8f7982000df4
def calculate(n1, n2, o):
    match o:
        case "add":
            return f"{int(n1, 2) + int(n2, 2):b}"
        case "subtract":
            return f"{int(n1, 2) - int(n2, 2):b}"
        case "multiply":
            return f"{int(n1, 2) * int(n2, 2):b}"
