# https://www.codewars.com/kata/57faf32df815ebd49e000117
def remove(st):
    words = st.split()
    result = []
    
    for w in words:
        result.append(w.rstrip("!"))
        
    return " ".join(result)
