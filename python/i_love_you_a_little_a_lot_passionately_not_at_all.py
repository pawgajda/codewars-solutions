# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
def how_much_i_love_you(nb_petals):
    answers = {
        0: "not at all",
        1: "I love you",
        2: "a little",
        3: "a lot",
        4: "passionately",
        5: "madly",
    }
    
    return answers[nb_petals % 6]
