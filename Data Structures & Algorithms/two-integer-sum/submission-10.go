func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int, len(nums))
    var pair int
    
    for i, vi := range nums {
        pair = target - vi
        
        if pairIdx, ok := hmap[pair]; ok {
            return []int{pairIdx, i}
        }

        hmap[vi] = i
    }
    return nil
}