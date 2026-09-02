class Solution:
    def numDecodings(self, s: str) -> int:
        # dp (bottom-up), time: O(n), space: O(1)
        if not s or s[0] == '0':
            return 0
            
        v1, v2 = 1, 1
        
        for i in range(1, len(s)):
            cur = 0                      # determine if it can be made into a single-digit number
            if s[i] != '0':
                cur += v2
                
            two_digit = int(s[i-1:i+1])   # determine if it can be made into a two-digits number
            if 10 <= two_digit <= 26:
                cur += v1
                
            if cur == 0:
                return 0
                
            v1, v2 = v2, cur
            
        return v2