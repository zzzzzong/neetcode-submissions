class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp, time: O(n^2), space: O(n^2)
        n = len(s)
        res_index, res_length = 0, 0
        dp = [[False] * n for _ in range(n)]


        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if res_length < (j - i + 1):
                        res_index = i
                        res_length = j - i + 1
        
        return s[res_index : res_index + res_length]