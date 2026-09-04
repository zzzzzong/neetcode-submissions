class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp, time: O(n), space: O(1)

        p2, p1 = 0, 0
        for c in cost:
            p2, p1 = p1, c + (p2 if p2 < p1 else p1)
        return p2 if p2 < p1 else p1