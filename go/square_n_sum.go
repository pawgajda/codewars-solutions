// https://www.codewars.com/kata/515e271a311df0350d00000f
package kata

import "math"

func SquareSum(numbers []int) int {
  var result int = 0
  for _, num := range numbers {
    result += int(math.Pow(float64(num), 2))
  }
  return result
}
