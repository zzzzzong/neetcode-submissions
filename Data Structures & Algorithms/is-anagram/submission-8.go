func isAnagram(s string, t string) bool {
    if len(s) != len(t) {return false}
    sCount, tCount := [26]int{}, [26]int{}

    for i := 0; i < len(s); i++ {
        sCount[s[i] - 'a'] += 1
        tCount[t[i] - 'a'] += 1
    }
    return sCount == tCount
}
