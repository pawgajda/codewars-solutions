// https://www.codewars.com/kata/55a2d7ebe362935a210000b2
package kata

import "sort"

func SmallestIntegerFinder(numbers []int) int {
  sort.Ints(numbers)
  return numbers[0]
}
