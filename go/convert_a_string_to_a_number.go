// https://www.codewars.com/kata/544675c6f971f7399a000e79
package kata

import "strconv"

func StringToNumber(str string) int {
      // your code here
      num, _ := strconv.Atoi(str)
      return num
}

