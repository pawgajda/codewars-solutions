// https://www.codewars.com/kata/576bb71bbbcf0951d5000044
package kata

func CountPositivesSumNegatives(numbers []int) []int {
  res := make([]int, 2)
  
  for _, num := range numbers {
    if num > 0 {
      res[0] += 1
    } else if num < 0 {
      res[1] += num
    }
  }
  return res
}
