func hasDuplicate(nums []int) bool {
    hmap := make(map[int]bool)

    for i := 0; i < len(nums); i++ {
        if hmap[nums[i]] {
            return true
        }

        hmap[nums[i]] = true
    }
    return false
}