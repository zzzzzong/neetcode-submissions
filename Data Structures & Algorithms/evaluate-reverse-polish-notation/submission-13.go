func evalRPN(tokens []string) int {
    stack := []int{}

    for _, t := range tokens {
        if t == "+" || t == "-" || t == "*" || t == "/" {
            left, right := stack[len(stack)-2], stack[len(stack)-1]
            stack = stack[:len(stack)-2]

            switch t {
            case "+": stack = append(stack, left+right)
            case "-": stack = append(stack, left-right)
            case "*": stack = append(stack, left*right)
            case "/": stack = append(stack, left/right)
            }
            continue
        }

        val := 0
        isNegative := false
        start := 0

        if t[0] == '-' {
            isNegative = true
            start = 1
        } else if t[0] == '+' {
            start = 1
        }

        for i := start; i < len(t); i++ {
            val = val*10 + int(t[i]-'0')
        }

        if isNegative {
            val = -val
        }

        stack = append(stack, val)
    }

    return stack[0]
}
