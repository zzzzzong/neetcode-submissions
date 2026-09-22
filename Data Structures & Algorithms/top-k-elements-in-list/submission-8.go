func topKFrequent(nums []int, k int) []int {
    // buckets x hashmap, time: O(3n), space: O(n)
    
    ans := []int{}
    // prepare hashmap
    hmap := make(map[int]int)
    
    for _, val := range nums{
        if _, ok := hmap[val]; ok {
            hmap[val] ++
            continue
        }
        hmap[val] = 1
    }

    // prepare buckets and put numbers in
    buckets := make([][]int, len(nums) + 1)

    for number, freq := range hmap {
        buckets[freq] = append(buckets[freq], number)
    }
    
    // get k numbers from the back
    for i := len(buckets) - 1; i > 0; i-- {
        for _, val := range buckets[i] {
            ans = append(ans, val)
            if len(ans) == k {
                return ans
            }
        }
    }
    return nil
}
