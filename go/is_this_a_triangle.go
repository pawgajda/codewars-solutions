package kata

func IsTriangle(a, b, c int) bool {
  if a < b + c && b < a + c && c < a + b {
    return true
  }
  return false
}
