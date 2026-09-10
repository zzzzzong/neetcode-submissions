func hasDuplicate(nums []int) bool {
    hmap := make(map[int]bool)

    for _, num := range nums{
        if hmap[num] {
            return true
        }
        hmap[num] = true
    }

    return false
}
