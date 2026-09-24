func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int)

    for curIdx, val := range nums {
        pairVal := target - val
        if pairIdx, ok := hmap[pairVal]; ok {
            return []int{pairIdx, curIdx}
        }

        hmap[val] = curIdx
    }

    return nil
}