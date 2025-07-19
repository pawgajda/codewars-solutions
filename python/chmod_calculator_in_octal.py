# https://www.codewars.com/kata/57f4ccf0ab9a91c3d5000054
def chmod_calculator(perm):
    # create a map of possible chmod permissions
    chmod = {
        "rwx": "7",
        "rw-": "6",
        "r-x": "5",
        "r--": "4",
        "-wx": "3",
        "-w-": "2",
        "--x": "1",
        "---": "0"
    }
    
    answer = []
    # iterate over possible keys in order
    for key in ["user", "group", "other"]:
        # append value to list if exists
        # otherwise append 0
        if key in perm.keys():
            # perm[key] == value
            value = perm[key]
            # use value of key as key for chmod map
            answer.append(chmod[value])
        else:
            answer.append("0")
    
    # convert answer list to string and return the string
    return ''.join(answer)
