# https://www.codewars.com/kata/57fa537f8b0760c7da000407
#
# attempt #1:
def diamonds_and_toads(sentence, fairy):
    if fairy == "good":
        result = {"ruby": 0, "crystal": 0}
    
        for c in sentence:
            match c:
                case "r": result["ruby"] += 1
                case "R": result["ruby"] += 2
                case "c": result["crystal"] += 1
                case "C": result["crystal"] += 2
                    
    if fairy == "evil":
        result = {"python": 0, "squirrel": 0}

        for c in sentence:
            match c:
                case "p": result["python"] += 1
                case "P": result["python"] += 2
                case "s": result["squirrel"] += 1
                case "S": result["squirrel"] += 2
                    
    return result
#
# attempt #2:
def diamonds_and_toads(sentence, fairy):
    result = {}

    if fairy == "good":
        result = {
            "ruby": sentence.count("r") + sentence.count("R") * 2,
            "crystal": sentence.count("c") + sentence.count("C") * 2,
        }
    else:
        result = {
            "python": sentence.count("p") + sentence.count("P") * 2,
            "squirrel": sentence.count("s") + sentence.count("S") * 2,
        }

    return result
