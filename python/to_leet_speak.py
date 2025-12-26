# https://www.codewars.com/kata/57c1ab3949324c321600013f
def to_leet_speak(s):
    leet_dict = {"A": "@", "B":"8", "C":"(", "D":"D", "E":"3", "F":"F", "G":"6", "H":"#",
                "I":"!", "J":"J", "K":"K", "L":"1", "M":"M", "N":"N", "O":"0", "P":"P",
                "Q":"Q", "R":"R", "S":"$", "T":"7", "U":"U", "V":"V", "W":"W", "X":"X",
                "Y":"Y", "Z":"2"}  
    leet_map = s.maketrans(leet_dict)
    leet_str = s.translate(leet_map)
    return leet_str
