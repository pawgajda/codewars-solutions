# https://www.codewars.com/kata/57de78848a8b8df8f10005b1
def how_much_coffee(events):
    valid_events = ["cw", "dog", "cat", "movie"]
    cups = 0
    
    for event in events:
        if event.isupper() and event.lower() in valid_events:
            cups += 2
        elif event.lower() in valid_events:
            cups += 1
    
    return cups if cups <= 3 else "You need extra sleep"
