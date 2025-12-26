// https://www.codewars.com/kata/56efc695740d30f963000557
//
// attempt #1:
package kata

import (
  "strings"
  "unicode"
)

func ToAlternatingCase(str string) string {
  var result string
  
  // iterate over runes and check their case
  for _, char := range str {
    // swap case, convert rune to string when doing so
    if unicode.IsUpper(char) {
      result = result + strings.ToLower(string(char))
    } else if unicode.IsLower(char) {
      result = result + strings.ToUpper(string(char))
    } else {
      result = result + string(char)
    }
  }
  return result
}
//
// attempt #2:
package kata

import "unicode"

func ToAlternatingCase(str string) string {
  var result []rune

  for _, char := range str {
    if unicode.IsUpper(char) {
        result = append(result, unicode.ToLower(char))
    } else if unicode.IsLower(char) {
        result = append(result, unicode.ToUpper(char))
    } else {
        result = append(result, char)
    }
  }
  return string(result)
}

