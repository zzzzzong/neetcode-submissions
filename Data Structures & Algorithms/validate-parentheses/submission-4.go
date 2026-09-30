func isValid(s string) bool {
    hmap := map[byte]byte {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    stack := []byte{}

    for i := 0; i < len(s); i++ {
        if s[i] == '(' || s[i] == '[' || s[i] == '{' {
            stack = append(stack, s[i])
            continue
        }

        if len(stack) == 0 {
            return false
        }

        pair := stack[len(stack) - 1]
        if hmap[s[i]] != pair {
            return false
        }

        stack = stack[:len(stack) - 1]
    }

    return len(stack) == 0
}
