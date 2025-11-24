# https://www.codewars.com/kata/5889177bf148eddd150002cc
def tiy_fizz_buzz(string):
    result = ""
    
    for char in string:
        # handle upper case vowels
        if char in ("A", "I", "U", "E","O"):
            result += "Iron Yard"
        # handle lower case vowels
        elif char in ("a", "i", "u", "e", "o"):
            result += "Yard"
        # handle upper case letters that are not vowels
        elif char.isupper():
            result += "Iron"
        # handle lower case letters and other characters
        else:
            result += char
    return result
