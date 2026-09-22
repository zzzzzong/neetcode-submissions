class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 3-pass, time: O(2n), space: O(2n)
        n = len(nums)
        left_products, right_products = [1] * n, [1] * n

        # left handed
        left_accumulate = 1
        for i in range(1, n):
            left_accumulate *= nums[i - 1]
            left_products[i] = left_accumulate
            
        # right handed
        right_accumulate = 1
        for i in range(n - 2, -1, -1):
            right_accumulate *= nums[i + 1]
            right_products[i] = right_accumulate
        
        # product them
        ans = [1] * n
        for i in range(n):
            ans[i] = left_products[i] * right_products[i]
        
        return ans