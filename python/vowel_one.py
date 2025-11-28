# https://www.codewars.com/kata/580751a40b5a777a200000a1
def vowel_one(s):
    result = ""
    
    for c in s:
        if c in "aiueoAIUEO":
            result += "1"
        else:
            result += "0"
            
    return result
