// https://www.codewars.com/kata/57a04da9e298a7ee43000111
package kata

func ReverseList(lst []int) []int {
  var result []int
  
  for i := len(lst) - 1; i >= 0; i-- {
    result = append(result, lst[i])
  }
  return result
}

