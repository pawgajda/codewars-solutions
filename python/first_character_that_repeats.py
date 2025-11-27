# https://www.codewars.com/kata/54f9f4d7c41722304e000bbb
def first_dup(s):
    for c in s:
        if s.count(c) > 1:
            return c
    return None
