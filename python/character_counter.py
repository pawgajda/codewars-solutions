# https://www.codewars.com/kata/56786a687e9a88d1cf00005d
def validate_word(word):
    lowercase_word = word.lower()
    count_map = {str(k): lowercase_word.count(k) for k in lowercase_word}
    count_list = list(count_map.values())
    return all([i == count_list[0] for i in count_list])
