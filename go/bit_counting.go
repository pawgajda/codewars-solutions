// https://www.codewars.com/kata/526571aae218b8ee490006f4
package kata

import (
  "strconv"
  "strings"
)

func CountBits(n uint) int {
  bin := strconv.FormatInt(int64(n), 2)
  return strings.Count(bin, "1")
}
