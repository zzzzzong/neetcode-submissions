class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n

        pre_1, pre_2 = 1, 2

        for i in range(3, n + 1):   # (n + 1) - 3
            cur = pre_1 + pre_2
            if i == n:
                return cur
            
            pre_1, pre_2 = pre_2, cur