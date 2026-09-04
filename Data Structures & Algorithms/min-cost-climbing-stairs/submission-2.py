class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp, time: O(n), space: O(n)

        cost.append(0)
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            if dp[i - 1] < dp[i - 2]:
                dp[i] = cost[i] + dp[i - 1]
                continue
            dp[i] = cost[i] + dp[i - 2]

        return dp[-1]