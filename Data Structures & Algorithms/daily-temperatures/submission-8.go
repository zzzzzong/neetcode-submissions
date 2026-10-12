func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures)
    ans := make([]int, n)
    stack := []int{}

    for i := 0; i < n; i++ {
        cur := temperatures[i]
        for len(stack) > 0 && cur > temperatures[stack[len(stack) - 1]] {
            idx := stack[len(stack) - 1]
            ans[idx] = i - idx
            stack = stack[:len(stack) - 1]
        }
        stack = append(stack, i)
    }

    return ans
}