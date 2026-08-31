class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        v1, v2 = 1, 2

        for i in range(3, n + 1):
            cur_val = v1 + v2
            if i == n:
                return cur_val

            v1, v2 = v2, cur_val