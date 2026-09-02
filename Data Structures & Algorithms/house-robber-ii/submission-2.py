class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 4: return max(nums)
        
        a, b, c = 0, 0, 0  # three conditions

        # not rob tail
        prev_1, prev_2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            cur = max(nums[i] + prev_1, prev_2)
            if i == n - 2:
                a = cur
                break
            
            prev_1, prev_2 = prev_2, cur

        # not rob tail and not rob head and tail

        prev_1, prev_2 = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            cur = max(nums[i] + prev_1, prev_2)
            if i == n - 3:
                b = cur
            if i == n - 1:
                c = cur
                break
            
            prev_1, prev_2 = prev_2, cur
        
        return max(a, b, c)