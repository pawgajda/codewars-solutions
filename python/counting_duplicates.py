# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
#
# attempt #1:
def duplicate_count(text):
    chars = {}

    for c in text.lower():
        if c.isalnum():
            if c not in chars:
                chars.setdefault(c, 1)
            else:
                chars[c] += 1
                
    return len([x for x in chars.values() if x > 1])
#
# attempt #2:
def duplicate_count(text):
    text = text.lower()

    seen = []
    count = 0
    
    for c in text:
        if c.isalnum():
            if text.count(c) > 1 and c not in seen:
                seen += c
                count += 1
    
    return count
#
# attempt #3:
def duplicate_count(text):
    text = text.lower()
    seen = []
    
    for c in text:
        if c.isalnum():
            if text.count(c) > 1 and c not in seen:
                seen.append(c)
                
    return len(seen)
