# https://www.codewars.com/kata/57faefc42b531482d5000123/train/python
def remove(s):
    if s.endswith("!"):
        # find how many '!' we have at the end of the string
        ex_idx = len(s) - len(s.rstrip("!"))
        # replace all '!' without touching the last ones
        # then add them to the end result
        return s[:-ex_idx].replace("!", "") + s[-ex_idx:]
    else:
        return s.replace("!", "")
