class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                # if i == operator，take the top 2 of the stack
                r, l = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(l + r)
                elif i == "-":
                    stack.append(l - r)
                elif i == "*":
                    stack.append(l * r)
                else:
                    stack.append(int(l / r))
        return stack[0]