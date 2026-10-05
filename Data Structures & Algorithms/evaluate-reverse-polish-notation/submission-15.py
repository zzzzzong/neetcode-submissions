class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = '+-*/'

        for i in tokens:
            if i not in operations:
                stack.append(int(i))
                continue

            right = stack.pop()
            left = stack.pop()
            
            if i == '+':
                stack.append(left + right)
                continue
            if i == '-':
                stack.append(left - right)
                continue
            if i == '*':
                stack.append(left * right)
                continue
            
            stack.append(int(left / right))
        
        return stack[0]