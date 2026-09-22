func twoSum(nums []int, target int) []int {
    hmap := make(map[int]int)  // hmap[value]index
    var pair int

    for i := 0; i < len(nums); i++ {
        pair = target - nums[i]
        if index, ok := hmap[pair]; ok {
            return []int{index, i}
        }    

        hmap[nums[i]] = i
    }   
    return nil

}