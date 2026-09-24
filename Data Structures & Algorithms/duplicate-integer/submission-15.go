func hasDuplicate(nums []int) bool {
    hmap := make(map[int]bool)

    for _,val := range nums {
        if _, ok := hmap[val]; ok {
            return true
        }

        hmap[val] = false
    }
    return false
}