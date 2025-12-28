# https://www.codewars.com/kata/583203e6eb35d7980400002a
def count_smileys(arr):
    count = 0
    valid_smileys = [
        ":)", ":-)", ":~)",
        ";)", ";-)", ";~)",
        ":D", ":-D", ":~D",
        ";D", ";-D", ";~D"
    ]
    
    for i in arr:
        if i in valid_smileys:
            count += 1
            
    return count
