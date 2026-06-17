class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == '+':
                stack[-2] += stack[-1]
                stack.pop()
                
            elif i == '-':
                stack[-2] -= stack[-1]
                stack.pop()

            elif i == '*':
                stack[-2] *= stack[-1]
                stack.pop()

            elif i == '/':
                stack[-2] = int(stack[-2] / stack[-1]) # here's the key of this question
                stack.pop()
            
            else:
                stack.append(int(i))
        
        return stack[0]