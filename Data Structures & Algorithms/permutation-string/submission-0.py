from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # pruning
        if len(s1) > len(s2): return False
        if s1 == s2: return True
        
        n = len(s1)
        m = len(s2)

        if n == 1: return s1 in s2
        
        # main logic
        c1 = Counter(s1)

        for left in range(m - n + 1):
            if s2[left] in c1:
                if Counter(s2[left: left + n]) == c1:
                    return True
            else:
                continue
        
        return False