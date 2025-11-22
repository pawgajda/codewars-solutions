// https://www.codewars.com/kata/5168bb5dfe9a00b126000018

// attempt #1:
package kata

import "strings"

func Solution(word string) string {
  tmp := strings.Split(word, "")
  var result []string
  
  for i := len(tmp) - 1; i >= 0; i-- {
    result = append(result, tmp[i])
  } 
  return strings.Join(result, "")
}

// attempt #2:
package kata

func Solution(word string) string {
  var result string
  
  for _, char := range word {
    result = string(char) + result
  }
  return result
}
