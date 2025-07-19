# https://www.codewars.com/kata/54da5a58ea159efa38000836

## First Solution:
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num


## Second Solution:
def find_it(seq):
    # create a map of item: counter
    seq_count = {str(k):0 for k in seq}
    # count the appearances of item
    for num in seq:
        seq_count[str(num)] += 1
    # interate thorugh the map and return first item with odd count
    for num, count in seq_count.items():
        if count % 2 != 0:
            return int(num)
