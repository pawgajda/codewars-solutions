# https://www.codewars.com/kata/57fae964d80daa229d000126
#
# attempt #1:
def remove(s):
    if len(s) != 0 and s[len(s) - 1] == "!":
        return s[:len(s) - 1]
    else:
        return s
#
# attempt #2:
def remove(s):
    if s[::-1].startswith("!"):
        return s[:-1]
    else:
        return s
