func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int, len(nums)/2)
    
    for i, vi := range nums {
        if pairIdx, ok := hmap[target-vi]; ok {
            return []int{pairIdx, i}
        }
        hmap[vi] = i
    }
    return nil
}