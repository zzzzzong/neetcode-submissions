class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_sum = nums[0]
        max_sum = cur_sum

        for i in range(1, len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum