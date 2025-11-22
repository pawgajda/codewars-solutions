// https://www.codewars.com/kata/5a00e05cc374cb34d100000d

// attempt #1:
package kata

func ReverseSeq(n int) []int {
  result := make([]int, n)
  i, j := n, 0
  
  for i > 0 && j < n {
    result[j] = i
    i--
    j++
  }
  return result
}

// attempt #2:
package kata

func ReverseSeq(n int) []int {
  var result []int
  
  for i := n; i > 0; i-- {
    result = append(result, i)
  }
  return result
}

// attempt #3:
package kata

func ReverseSeq(n int) (result []int) {
  for i := n; i > 0; i-- {
    result = append(result, i)
  }
  return
}
