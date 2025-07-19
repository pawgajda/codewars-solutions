# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    result = []
    # treat the string like list and iterate over every other element
    for i in range(0, len(s), 2):
        # check if potential adjecent character is within list range
        if i + 1 < len(s):
            # append i and i + 1 character to result
            result.append(s[i] + s[i + 1])
        # if there is no adjecent character within list range
        else:
            # add underscore "_"
            result.append(s[i] + "_")
    return result
