// https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
package kata

import "strings"

func StringToArray(str string) []string {
  var result []string = strings.Fields(str)
  return result
}
