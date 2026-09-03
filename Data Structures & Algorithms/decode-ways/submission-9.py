class Solution:
    def numDecodings(self, s: str) -> int:
        # dp (bottom-up), time: O(n), space: O(1)
        if not s:
            return 0
            
        dp1, dp2 = 1, 0
        
        for i in range(len(s) - 1, -1, -1):
            dp = 0 if s[i] == '0' else dp1
            
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                dp += dp2
                
            dp2, dp1 = dp1, dp
            
        return dp1