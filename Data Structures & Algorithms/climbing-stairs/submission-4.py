class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        v1, v2 = 1, 2

        for _ in range(3, n + 1):
            v1, v2 = v2, v1 + v2
        
        return v2