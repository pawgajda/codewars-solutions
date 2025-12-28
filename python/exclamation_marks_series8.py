# https://www.codewars.com/kata/57fafd0ed80daac48800019f
def remove(string: str) -> str:
    return string.replace("!", "") + string.count("!") * "!"
