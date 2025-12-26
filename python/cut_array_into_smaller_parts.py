# https://www.codewars.com/kata/58ac59d21c9e1d7dc5000150
def make_parts(arr, chunk_size):
    result = []

    for i in range(0, len(arr), chunk_size):
        result.append(arr[i:i + chunk_size])
        
    return result
