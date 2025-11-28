# https://www.codewars.com/kata/57cff961eca260b71900008f
def is_vow(inp):
    result = []

    for code in inp:
        if chr(code) in "aiueo":
            result.append(chr(code))
        else:
            result.append(code)
            
    return result
