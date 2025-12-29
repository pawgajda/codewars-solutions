// https://www.codewars.com/kata/526571aae218b8ee490006f4
//
// attempt #1:
package kata

import (
  "strconv"
  "strings"
)

func CountBits(n uint) int {
  bin := strconv.FormatInt(int64(n), 2)
  return strings.Count(bin, "1")
}
//
// attempt #2:
package kata

import "math/bits"

func CountBits(n uint) int {
    return bits.OnesCount(n)
}
