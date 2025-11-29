# https://www.codewars.com/kata/581b29b549b2c0daeb001454
#
# attempt #1:
def bang_contain_string(s,history):
    hist = history.split("\n")
    hist = [i.strip() for i in hist]
    # reverse the list because we look for most recent command
    hist = list(reversed(hist))
 
    for entry in hist:
        if s in entry:
            # parse found entry
            return " ".join(entry.split(" ")[2:])

    return f"!{s}: event not found"
#
# attempt #2:
def bang_contain_string(s,history):
    hist = history.split("\n")
    hist = [i.strip() for i in hist]
    # remove numbers from hist entries
    hist = [" ".join(i.split()[1:]) for i in hist]
    # reverse the list because we look for most recent command
    hist = list(reversed(hist))
 
    for entry in hist:
        if s in entry:
            # parse found entry
            return entry

    return f"!{s}: event not found"
