func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers) - 1

	for left < right {
		summ := numbers[left] + numbers[right]
		if summ == target {
			return []int{left + 1, right + 1}
		}
		if summ < target {
			left++
			continue
		}
		right--

	}
	return nil
}
