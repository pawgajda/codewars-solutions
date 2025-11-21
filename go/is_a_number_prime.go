// https://www.codewars.com/kata/5262119038c0985a5b00029f
package kata

import "math"

func IsPrime(n int) bool {
  //your code here
  if n <= 1 {
    return false
  }
  
  m := int(math.Sqrt(float64(n)))
  
  for i := 2; i < m + 1; i++ {
    if n % i == 0 {
      return false
    }
  }
  return true
}
