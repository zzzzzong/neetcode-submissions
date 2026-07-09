// brute force, time: O(n^2), space: O(1)

func hasDuplicate(nums []int) bool {
    sort.Ints(nums) // sorting 
    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1] {
            return true
        }
    }
    return false
}
