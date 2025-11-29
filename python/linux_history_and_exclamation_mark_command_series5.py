# https://www.codewars.com/kata/581b29b549b2c0daeb001454
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
