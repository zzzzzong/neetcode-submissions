class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0

        for char in nums:
            cur += char
            if cur > ans:
                ans = cur
            
            if cur < 0:
                cur = 0
        
        return ans