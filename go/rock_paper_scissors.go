// https://www.codewars.com/kata/5672a98bdbdd995fad00000f
package kata

func Rps(p1, p2 string) string {
  // key beats value
  victoryMap := map[string]string{"rock": "scissors", "scissors": "paper", "paper": "rock"}
  if victoryMap[p1] == p2 {return "Player 1 won!"}
  if victoryMap[p2] == p1 {return "Player 2 won!"}
  return "Draw!"
}
