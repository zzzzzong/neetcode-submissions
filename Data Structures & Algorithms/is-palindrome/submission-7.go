func isPalindrome(s string) bool {
    left, right := 0, len(s) - 1

    for left < right {
        if !isAlnum(s[left]) {
            left++
            continue
        }

        if !isAlnum(s[right]) {
            right--
            continue
        }

        if lower(s[left]) != lower(s[right]){
            return false
        }
        left++
        right--
    }
    return true
}



func isAlnum(char byte) bool {
    if ('a' <= char && char <= 'z') ||
        ('A' <= char && char <= 'Z') ||
        ('0' <= char && char <= '9') {
            return true
        }
    return false
}

func lower(char byte) byte {
    if 'A' <= char && char <= 'Z' {
        return char + 32
    }

    return char
}