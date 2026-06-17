class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h1 = {}
        h2 = {}

        for i in range(len(s)):
            if s[i] in h1:
                h1[s[i]] += 1
            if s[i] not in h1:
                h1[s[i]] = 1
            
            if t[i] in h2:
                h2[t[i]] += 1
            else:
                h2[t[i]] = 1
        
        return h1 == h2
