class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp, time: O(n), space: O(1)

        cost.append(0)
        n = len(cost)
        prev_1, prev_2 = cost[0], cost[1]

        for i in range(2, n):
            if prev_1 < prev_2:
                prev_1, prev_2 = prev_2, cost[i] + prev_1
                continue
            prev_1, prev_2 = prev_2, cost[i] + prev_2

        return min(prev_1, prev_2)