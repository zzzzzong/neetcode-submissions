class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        def expand(index: int) -> None:
            # odd length
            nonlocal ans
            left, right = index, index
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
            
            # even length
            left, right = index, index + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1

        for i in range(n):
            expand(i)
        
        return ans