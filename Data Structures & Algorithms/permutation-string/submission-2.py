class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # pruning
        n, m = len(s1), len(s2)
        if n > m: 
            return False
        
        # 使用長度為 26 的列表代替 Counter，底層查找和比較速度更快
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        if s1_count == s2_count:
            return True

        # main logic
        # fixed sized sliding window
        # Time: O(m) where m is the length of s2
        # Space: O(1), using only a constant number of variables

        for i in range(n, m):
            s2_count[ord(s2[i]) - ord('a')] += 1

            s2_count[ord(s2[i - n]) - ord('a')] -= 1
            
            # 3. 每次移動完，直接比較兩個長度 26 的陣列是否相等
            if s1_count == s2_count:
                return True
                
        return False