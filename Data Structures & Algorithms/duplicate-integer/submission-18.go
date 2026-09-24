func hasDuplicate(nums []int) bool {
    hmap := make(map[int]bool)

    for _,val := range nums {
        if hmap[val] {
            return true
        }

        hmap[val] = true
    }
    return false
}