// https://www.codewars.com/kata/57a049e253ba33ac5e000212
package kata

func Factorial(n int) int {
  if n == 0 {
    return 1
  } else {
    return n * Factorial(n - 1)
  }
}

