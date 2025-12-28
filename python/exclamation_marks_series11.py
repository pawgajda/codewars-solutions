# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
def replace_exclamation(st):
    return st.translate(st.maketrans("AEIOUaeiou", "!!!!!!!!!!"))
