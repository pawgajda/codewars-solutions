# ttps://www.codewars.com/kata/5672a98bdbdd995fad00000f
def rps(p1, p2):
    # key wins over value
    victory_map = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    
    if p1 == p2:
        return "Draw!"
    elif victory_map[p1] == p2:
        return "Player 1 won!"
    elif victory_map[p2] == p1:
        return "Player 2 won!"
