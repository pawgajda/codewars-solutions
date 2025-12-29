// https://www.codewars.com/kata/57a5c31ce298a7e6b7000334
// 
// attempt #1:
package kata

import (
  "math"
  "strconv"
)

func BinToDec(bin string) int {
  x := len(bin) - 1
  result := 0

  for _, bit := range bin {
    b, _ := strconv.Atoi(string(bit))
    result += b * int(math.Pow(float64(2), float64(x)))
    x -= 1
  }
  return result
}
//
// attempt #2:
package kata

import "strconv"

func BinToDec(bin string) int {
  num, _ := strconv.ParseInt(bin, 2, 64)
  return int(num)
}
