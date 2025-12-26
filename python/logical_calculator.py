# https://www.codewars.com/kata/57096af70dad013aa200007b
#
# attempt #1:
def logical_calc(array, op):
    match op:
        case "AND":
            return all(array)
        case "OR":
            return any(array)
        case "XOR":
            xor = array[0]
            for x in array[1:]:
                xor ^= x
            return xor
#
# attampt #2:
def logical_calc(array, op):
    result = array[0]
    
    for i in array[1:]:
        if op == "AND":
            result &= i
        elif op == "OR":
            result |= i
        elif op == "XOR":
            result ^= i
            
    return result
