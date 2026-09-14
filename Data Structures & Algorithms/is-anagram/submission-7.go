func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	var counts [26]int
	for i := 0; i < len(s); i++ {
		counts[s[i]-'a']++
	}

	for i := 0; i < len(t); i++ {
		counts[t[i]-'a']--
		if counts[t[i]-'a'] < 0 {
			return false
		}
	}

	return true
}
