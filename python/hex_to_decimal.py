# https://www.codewars.com/kata/57a4d500e298a7952100035d
#
# attempt #1:
def hex_to_dec(s):
    result = 0
    p = len(s) - 1
    
    for i in s:
        match i:
            case "a" | "A":
                val = 10
            case "b" | "B":
                val = 11
            case "c" | "C":
                val = 12
            case "d" | "D":
                val = 13
            case "e" | "E":
                val = 14
            case "f" | "F":
                val = 15
            case _:
                val = i
        
        result += int(val) * 16 ** p
        p -= 1
        
    return result
#
# attempt #2:
def hex_to_dec(s):
    return int(s, 16)
