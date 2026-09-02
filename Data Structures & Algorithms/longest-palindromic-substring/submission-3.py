class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers, time: O(n^2), space: O(n)
        n = len(s)
        res_index, res_length = 0, 0

        for i in range(n):
            # odd length
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > res_length:
                    res_index = left
                    res_length = right - left + 1
                
                left -= 1
                right += 1
            
            # even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > res_length:
                    res_index = left
                    res_length = right - left + 1
                
                left -= 1
                right += 1
        
        return s[res_index: res_index + res_length]