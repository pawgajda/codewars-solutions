# https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a
def replace_all(obj, find, replace):
    if type(obj) is str:
        return obj.replace(find, replace)
    elif type(obj) is list:
        for i, v in enumerate(obj):
            if v == find:
                obj[i] = replace
        return obj
