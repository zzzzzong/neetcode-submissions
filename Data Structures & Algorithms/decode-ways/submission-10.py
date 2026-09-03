class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        if n == 1:
            return 1

        dp2 = 1
        dp1 = 0 if s[n - 1] == '0' else 1
        
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1
                if 10 <= int(s[i:i+2]) <= 26:
                    dp += dp2
                    
            dp2 = dp1
            dp1 = dp
            
        return dp1