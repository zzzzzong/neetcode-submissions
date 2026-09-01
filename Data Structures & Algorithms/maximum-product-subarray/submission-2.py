class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp, time: O(n), space: O(1)

        dp_max, dp_min = nums[0], nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]

            dp_max, dp_min = max(cur, cur * dp_max, cur * dp_min), min(cur, cur * dp_max, cur * dp_min)

            ans = max(ans, dp_max)

        return ans