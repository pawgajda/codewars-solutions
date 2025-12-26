# https://www.codewars.com/kata/5202ef17a402dd033c000009
def title_case(title, minor_words=''):
    result = []

    for index, word in enumerate(title.split()):
        # first word should always be title case
        if index == 0:
            result.append(word.capitalize())
        # if anything from minor_words matches our word, use lower case for that word
        elif any([word.lower() == x.lower() for x in minor_words.split()]):
            result.append(word.lower())
        # else use title case
        else:
            result.append(word.capitalize())

    return " ".join(result)

