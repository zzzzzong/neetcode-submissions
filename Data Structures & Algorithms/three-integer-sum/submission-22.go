import "slices"

func threeSum(nums []int) [][]int {
    n := len(nums)
    var ans [][]int
    slices.Sort(nums)  // new toy lol

    for pivotIdx := 0; pivotIdx < n-2; pivotIdx++ {
        pivotVal := nums[pivotIdx]

        if pivotVal + nums[n-1] + nums[n-2] < 0 { continue }
        if pivotIdx > 0 && pivotVal == nums[pivotIdx-1] { continue }
        if pivotVal > 0 { break }

        left, right := pivotIdx + 1, n-1

        for left < right {
            curSum := pivotVal + nums[left] + nums[right]

            if curSum == 0 {
                ans = append(ans, []int{pivotVal, nums[left], nums[right]})
                
                left++
                for left < right && nums[left] == nums[left-1] {
                    left++
                }

                right--
                for left < right && nums[right] == nums[right+1] {
                    right--
                }
                continue
            }

            if curSum < 0 {
                left++
                for left < right && nums[left] == nums[left-1] {
                    left++
                }
                continue
            }

            right--
            for left < right && nums[right] == nums[right+1] {
                right--
            }
        }
    }

    return ans
}
