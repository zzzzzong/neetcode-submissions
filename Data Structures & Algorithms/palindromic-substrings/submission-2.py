class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        for cur in range(n):
            
            left, right = cur, cur
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

            left, right = cur, cur + 1
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans