# https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in "aiueoAIUEO":
            count += 1
    return count
