func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int, len(nums))  // hmap[value]index
    var pair int

    for i := 0; i < len(nums); i++ {
        pair = target - nums[i]

        for idx, val := range nums {
            pair = target - val
            
            if pairIndex, ok := hmap[pair]; ok {
                return []int{pairIndex, idx}
            }

            hmap[val] = idx
        }
    }
    return nil
}