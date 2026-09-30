class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in '+-*/':
                right = stack.pop()
                left = stack.pop()
                if t == '+':
                    stack.append(left + right)
                    continue
                if t == '-':
                    stack.append(left - right)
                    continue
                if t == '*':
                    stack.append(left * right)
                    continue
                if t == '/':
                    stack.append(int(left / right))
                    continue
            
            stack.append(int(t))
            
        return stack[0]