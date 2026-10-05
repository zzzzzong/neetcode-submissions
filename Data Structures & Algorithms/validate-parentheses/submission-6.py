class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
                continue
            
            if not stack:
                return False
            
            if hmap[s[i]] != stack.pop():
                return False
        
        return not stack