class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''

        def expand(cur: int) -> None:
            nonlocal ans

            left, right = cur, cur
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            if right - left - 1 > len(ans):
                ans = s[left + 1: right]

            left, right = cur, cur + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            if right - left - 1 > len(ans):
                ans = s[left + 1: right]
            
        for mid in range(n):
            expand(mid)
        
        return ans