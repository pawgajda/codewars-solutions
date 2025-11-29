# https://www.codewars.com/kata/5815fd7441e062463d0000f8
def bang_minus_n(n,history):
    hist = history.split("\n")
    
    if n > len(hist):
        return f"!{-n}: event not found"
    else:
        hist_entry = hist[-n].split()
        hist_cmd = ' '.join(hist_entry[1:])
        return hist_cmd
