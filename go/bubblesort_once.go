// https://www.codewars.com/kata/56b97b776ffcea598a0006f2
package kata

func BubblesortOnce(numbers []int) []int {
  // copy array
  arr := make([]int, len(numbers))
  copy(arr, numbers)

  // bubble sort once
  for i := 0; i < len(arr) - 1; i++ {
    if arr[i] > arr[i + 1] {
      arr[i], arr[i + 1] = arr[i + 1], arr[i]
    }
  }
  return arr
}

