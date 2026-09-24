func isAnagram(s string, t string) bool {
    if len(s) != len(t) {return false}
    
    counter := [26]int{}

    for i := 0; i < len(s); i++ {
        counter[s[i] - 'a'] ++
        counter[t[i] - 'a'] --
    }

    for _, val := range counter {
        if val != 0 {
            return false
        }
    }

    return true
}