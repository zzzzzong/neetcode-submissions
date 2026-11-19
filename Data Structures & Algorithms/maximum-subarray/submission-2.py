class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')
        cur = 0
        left = 0

        for right in range(len(nums)):
            cur += nums[right]
            if cur > ans:
                ans = cur
            
            if cur < 0:
                left = right + 1
                cur = 0
        
        return ans