func longestConsecutive(nums []int) int {
    hmap := make(map[int]bool)
    for i := 0; i < len(nums); i++ {
        hmap[nums[i]] = true
    }

    ans := 0
    for index := range hmap {
        if !hmap[index-1] {
            curIndex := index
            count := 1

            for hmap[curIndex+1] {
                curIndex++
                count++
            }

            if count > ans {
                ans = count
            }
        }
    }

    return ans

}
