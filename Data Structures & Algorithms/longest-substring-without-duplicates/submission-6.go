func lengthOfLongestSubstring(s string) int {
    hmap := make(map[byte]bool)
    left := 0
    ans := 0

    for right, _ := range s {
        for hmap[s[right]] {
            hmap[s[left]] = false
            left++
        }

        hmap[s[right]] = true
        if ans < right - left + 1 {
            ans = right - left + 1
        }
    }
    return ans
}
