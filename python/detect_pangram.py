# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
#
# attempt #1:
def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = {}
    
    for c in st.lower():
        if c.isalpha():
            if c not in result:
                result.setdefault(c, 1)
            else:
                result[c] += 1

    return "".join(sorted(result.keys())) == alphabet
#
# attempt #2:
def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    for c in st.lower():
        if c.isalpha() and c not in result:
            result += c
    
    return "".join(sorted(result)) == alphabet
#
# attempt #3:
def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for l in alphabet:
        if l not in st.lower():
            return False

    return True
