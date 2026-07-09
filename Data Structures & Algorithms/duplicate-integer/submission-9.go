// hashmap, time: O(n), space: O(n)

func hasDuplicate(nums []int) bool {
    hmap := make(map[int]bool)
    for _, char := range nums {
        if hmap[char] {
            return true
        }
        hmap[char] = true
    }
    return false
}
