class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        for char in tokens:
            if char not in '+-*/':
                stack.append(int(char))
                continue
            
            right = stack.pop()
            left = stack.pop()

            if char == '+':
                stack.append(left + right)
                continue
            if char == '-':
                stack.append(left - right)
                continue
            if char == '*':
                stack.append(left * right)
                continue

            stack.append(int(left / right))
            continue
        
        return stack[0]