class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        pre_1, pre_2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(nums[i] + pre_1, pre_2)
            
            pre_1, pre_2 = pre_2, cur
        
        return pre_2