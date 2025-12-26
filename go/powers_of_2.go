// https://www.codewars.com/kata/57a083a57cb1f31db7000028
package kata

import "math"

func PowersOfTwo(n int) []uint64 {
  var result []uint64
  
  for i := 0; i <= n; i++ {
    result = append(result, uint64(math.Pow(2, float64(i))))
  }
  return result
}
