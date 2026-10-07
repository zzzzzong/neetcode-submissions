class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed window sliding, time: O(N), space: O(m)
        if len(s1) > len(s2):
            return False
        
        n, m = len(s1), len(s2)
        count_1, count_2 = [0] * 26, [0] * 26

        # first half
        for i in range(n):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1
        
        if count_1 == count_2:
            return True
        
        # remain
        for i in range(n, m):
            count_2[ord(s2[i]) - ord('a')] += 1
            count_2[ord(s2[i - n]) - ord('a')] -= 1
            
            if count_1 == count_2:
                return True
    
        return False