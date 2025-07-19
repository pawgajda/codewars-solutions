# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    # your code here
    if len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    elif len(names) >= 4:
        # subtract two "known" names
        other_names = len(names) - 2
        return "{}, {} and {} others like this".format(names[0], names[1], other_names)
    else:
        return "no one likes this"
