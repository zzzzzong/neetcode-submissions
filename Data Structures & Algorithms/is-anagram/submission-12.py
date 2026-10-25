class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        counter = [0] * 26
        for i in range(n):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for content  in counter:
            if content != 0:
                return False
            
        return True