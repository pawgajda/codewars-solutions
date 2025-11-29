# https://www.codewars.com/kata/5814bf3f3db1ffc0180000d3
def bang_n(n, history):
    hist = history.split("\n")
    
    if n > len(hist):
        return f"!{n}: event not found"
    else:
        hist_entry = hist[n - 1].split()
        hist_cmd = ' '.join(hist_entry[1:])
        return hist_cmd
