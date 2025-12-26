# https://www.codewars.com/kata/52223df9e8f98c7aa7000062
#
# attempt #1:
def rot13(message):
    result = ""
    
    for c in message:
        if c.isalpha():
            # for char up to m, add 13
            if ord(c.lower()) <= 109:
                result += chr(ord(c) + 13)
            # for chars starting with n, subtract 13
            else:
                result += chr(ord(c) - 13)
        else:
            # skip everything else
            result += c
            
    return result
#
# attempt #2:
def rot13(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    charmap = {
        x: chr(ord(x) + 13) if ord(x.lower()) <= 109 else chr(ord(x) - 13)
               for x in alphabet
    }

    return message.translate(message.maketrans(charmap))
#
# attempt #3:
def rot13(message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    translation = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    
    return message.translate(message.maketrans(alphabet, translation))
#
# attempt #4:
def rot13(message):
    result = ""
    
    for c in message:
        if c.isalpha():
            if c.islower():
                base = "a"
            else:
                base = "A"

            result += chr((ord(c) - ord(base) + 13) % 26 + ord(base))
        else:
            result += c
    
    return result
