// https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
package kata

import "strings"

func IsPalindrome(str string) bool {
  // convert string to lover case
  str = strings.ToLower(str)

  left := 0
  right := len(str) - 1
  
  for left < right {
    if str[left] != str[right] {
      return false
    }
    left += 1
    right -= 1
  }
  return true
}
