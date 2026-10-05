func dailyTemperatures(temperatures []int) []int {
    stack := []int{}
    ans := make([]int, len(temperatures))

    for idx, val := range temperatures {
        for len(stack) > 0 && val > temperatures[stack[len(stack)-1]] {
            prev_idx := stack[len(stack) - 1]
            ans[prev_idx] = idx - prev_idx
            stack = stack[:len(stack) - 1]
        }

        stack = append(stack, idx)
    }

    return ans
}
