class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers(middle outward), time: O(n^2), space: O(1)
        n = len(s)
        if n < 2:
            return s
            
        res_index, res_length = 0, 1

        for i in range(n):
            # odd length
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # optimize: only compare the length when the loop is over instead of every round
            cur_len = right - left - 1
            if cur_len > res_length:
                res_index = left + 1
                res_length = cur_len
            
            # even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            cur_len = right - left - 1
            if cur_len > res_length:
                res_index = left + 1
                res_length = cur_len
        
        return s[res_index: res_index + res_length]