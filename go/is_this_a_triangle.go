// https://www.codewars.com/kata/56606694ec01347ce800001b
package kata

func IsTriangle(a, b, c int) bool {
  if a < b + c && b < a + c && c < a + b {
    return true
  }
  return false
}
