// brute force, time: O(n^2), space: O(1)

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
