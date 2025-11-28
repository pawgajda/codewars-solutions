# https://www.codewars.com/kata/5680781b6b7c2be860000036
def vowel_indices(word):
    result = []
    # here indexing starts from 1 :(
    idx = 1
    for c in word:
        if c in "aiueoyAIUEOY":
            result.append(idx)
        idx += 1
    return result
