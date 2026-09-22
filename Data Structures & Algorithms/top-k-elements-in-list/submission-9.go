func topKFrequent(nums []int, k int) []int {
    // buckets x hashmap, time: O(3n), space: O(n)
    
    // prepare hashmap
    n := len(nums)
    hmap := make(map[int]int, n) // 預先指定 map 容量，避免動態擴容
    for _, val := range nums {
        hmap[val]++
    }

    // 用兩個一維陣列模擬桶子（鄰接表）
    // head[f] 儲存頻率為 f 的最後一個數字
    // next[i] 儲存鏈結中的下一個節點
    head := make([]int, n+1)
    next := make([]int, len(hmap)+1)
    
    // 初始化 head 陣列為 -1，代表該頻率目前是空的
    for i := range head {
        head[i] = -1
    }

    // 將數字放入一維鏈結桶子中
    // 這裡我們給每個不重複的數字一個唯一的序號 id (從 1 開始)
    uniqueNums := make([]int, len(hmap)+1)
    id := 1
    for number, freq := range hmap {
        uniqueNums[id] = number
        
        // 鏈結串接：新節點指向舊的 head，head 再更新為新節點
        next[id] = head[freq]
        head[freq] = id
        id++
    }

    // 預先分配好答案的空間，完全不需要 append
    ans := make([]int, k)
    idx := 0

    // 從後往前掃描頻率，順著鏈結取出數字
    for freq := n; freq > 0; freq-- {
        for id := head[freq]; id != -1; id = next[id] {
            ans[idx] = uniqueNums[id]
            idx++
            if idx == k {
                return ans
            }
        }
    }

    return ans
}
