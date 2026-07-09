class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        for left in range(len(nums) - k + 1):
            res.append(max(nums[left: left + k]))
        
        return res