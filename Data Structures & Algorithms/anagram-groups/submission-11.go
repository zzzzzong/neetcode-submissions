func groupAnagrams(strs []string) [][]string {
    hmap := make(map[[26]int][]string)

    for i := 0; i < len(strs); i++ {
        var counter [26]int
        word := strs[i]
        
        for j := 0; j < len(word); j++ {
            counter[word[j]-'a']++
        }
        
        hmap[counter] = append(hmap[counter], word)
    }

    ans := make([][]string, 0, len(hmap))
    for _, val := range hmap {
        ans = append(ans, val)
    }

    return ans
}
