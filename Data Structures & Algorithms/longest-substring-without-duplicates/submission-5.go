func lengthOfLongestSubstring(s string) int {
    hmap := make(map[byte]bool, len(s))
    left := 0
    ans := 0

    for right := 0; right < len(s); right++ {
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
