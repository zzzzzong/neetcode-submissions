func characterReplacement(s string, k int) int {
    windowCounter := make([]int, 26)
    ans := 0
    mostFreq := 0
    left := 0

    for rightIdx, rightVal := range s {
        windowCounter[rightVal - 'A']++

        if windowCounter[rightVal - 'A'] > mostFreq {
            mostFreq = windowCounter[rightVal - 'A']
        }

        for rightIdx - left + 1 - mostFreq > k {
            windowCounter[s[left] - 'A']--
            left++
        }

        if rightIdx - left + 1 > ans {
            ans = rightIdx - left + 1
        }
    }

    return ans

}
