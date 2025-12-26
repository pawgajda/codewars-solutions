// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
package kata

func CalculateYears(years int) (result [3]int) {
  var catYears int = 0
  var dogYears int = 0
  
  for i := 1; i <= years; i++ {
    if i == 1 {
      catYears += 15
      dogYears += 15
    } else if i == 2 {
      catYears += 9
      dogYears += 9
    } else {
      catYears += 4
      dogYears += 5
    }
  }
  result = [3]int{years, catYears, dogYears}
  return result
}
