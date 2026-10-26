class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in '([{':
                stack.append(char)
                continue
            
            if not stack:
                return False
            pair = stack.pop()
            if hmap[char] != pair:
                return False
        
        return not stack