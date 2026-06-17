class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                peek = stack.pop()
                if s[i] == ")" and peek != "(":
                    return False
                if s[i] == "]" and peek != "[":
                    return False
                if s[i] == "}" and peek != "{":
                    return False
        
        return len(stack) == 0