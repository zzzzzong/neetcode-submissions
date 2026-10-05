func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures)
	ans := make([]int, n)
	stack := make([]int, 0, n)

	for idx, val := range temperatures {
		for nStack := len(stack); nStack > 0 && val > temperatures[stack[nStack-1]]; nStack = len(stack) {
			prev_idx := stack[nStack-1]
			ans[prev_idx] = idx - prev_idx
			stack = stack[:nStack-1]
		}
		stack = append(stack, idx)
	}

	return ans
}