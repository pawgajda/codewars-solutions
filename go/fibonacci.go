// https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af
package kata


func Fib(n int) int {
  if n < 2 {
    return n
  } else {
    return Fib(n - 1) + Fib(n - 2)
  }
}
