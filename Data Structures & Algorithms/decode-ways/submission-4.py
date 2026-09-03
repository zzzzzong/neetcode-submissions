class Solution:
    def numDecodings(self, s: str) -> int:
        # dp (bottom-up), time: O(n), space: O(1)
        if not s or s[0] == '0':
            return 0
            
        tens_place, ones_place = 1, 1 
        
        for i in range(1, len(s)):
            cur_ways = 0

            # check if could be a single-digit number
            if s[i] != '0':
                cur_ways += ones_place
            
            # two-digit number
            two_digit = int(s[i-1 : i+1])
            if 10 <= two_digit <= 26:
                cur_ways += tens_place
                
            if cur_ways == 0:
                return 0
                
            tens_place, ones_place = ones_place, cur_ways
            
        return ones_place