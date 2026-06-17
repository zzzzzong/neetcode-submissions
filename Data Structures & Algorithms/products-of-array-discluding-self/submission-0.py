class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        loop two times:
            first time to product the elements left side form the target
            second time to product the right sides.
        '''
        n = len(nums)
        res = [1] * n

        # left part
        left = 1
        for i in range(n):
            res[i] *= left
            left *=  nums[i]
        
        # right part
        right = 1
        for j in range(-1, -(n+1), -1):
            res[j] *= right
            right *= nums[j]
        
        return res