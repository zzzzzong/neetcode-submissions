func productExceptSelf(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    ans[0] = 1
    
    left_accumulate := 1
    for i := 1; i < n; i++ {
        left_accumulate *= nums[i - 1]
        ans[i] = left_accumulate
    }

    right_accumulate := 1
    for i := n - 2; i >= 0; i-- {
        right_accumulate *= nums[i + 1]
        ans[i] *= right_accumulate
    }

    return ans
}
