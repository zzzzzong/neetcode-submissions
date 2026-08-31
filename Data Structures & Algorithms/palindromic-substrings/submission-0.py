class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointers outward expansion, time: O(n^2), space: O(1)
        n = len(s)
        if n < 2: 
            return n
        
        count = 0

        start, end = 0, 0

        def outward_expand(left: int, right: int) -> tuple:
            while left >= 0 and right < n and s[left] == s[right]:
                nonlocal count
                count += 1
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(n):
            l1, r1 = outward_expand(i, i)
            if (r1 - l1) > (end - start):
                start, end = l1, r1
                
            l2, r2 = outward_expand(i, i + 1)
            if (r2 - l2) > (end - start):
                start, end = l2, r2

        return count