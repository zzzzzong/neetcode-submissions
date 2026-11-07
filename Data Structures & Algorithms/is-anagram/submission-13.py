class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if len(t) != n:
            return False

        counter = [0] * 26
        k = ord('a')
        for i in range(n):
            counter[ord(s[i]) - k] += 1
            counter[ord(t[i]) - k] -= 1
        
        for element in counter:
            if element != 0:
                return False
        
        return True