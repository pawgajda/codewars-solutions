# https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    # convert input to lowercase
    s = text.lower()
    # create letter to number mapping
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_map = {v: str(k + 1) for k, v in enumerate(letters)}
    # return result as string created by using list comprehension
    return ' '.join([letter_map[c] for c in list(s) if c in letter_map.keys()])
