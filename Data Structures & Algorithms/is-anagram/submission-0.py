class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ss = []
        tt = []

        for i in range(len(s)):
            ss.append(s[i])
            tt.append(t[i])
        
        ss.sort()
        tt.sort()

        return ss == tt