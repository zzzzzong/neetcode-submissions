class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        tmp = 1
        for left in range(1, n):
            tmp *= nums[left - 1]
            res[left] *= tmp
        tmp = 1
        for right in range(n - 2, -1, -1):
            tmp *= nums[right + 1]
            res[right] *= tmp
        
        return res