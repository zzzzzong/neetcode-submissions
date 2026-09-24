func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left < right {
		if !isAlphanumeric(s[left]) {
			left++
			continue
		}
		if !isAlphanumeric(s[right]) {
			right--
			continue
		}

		if toLower(s[left]) != toLower(s[right]) {
			return false
		}

		left++
		right--
	}

	return true
}

func isAlphanumeric(ch byte) bool {
	return (ch >= 'a' && ch <= 'z') || 
	       (ch >= 'A' && ch <= 'Z') || 
	       (ch >= '0' && ch <= '9')
}

func toLower(ch byte) byte {
	if ch >= 'A' && ch <= 'Z' {
		return ch + 32
	}
	return ch
}
