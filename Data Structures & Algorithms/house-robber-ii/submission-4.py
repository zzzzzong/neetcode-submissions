class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp (one-pass), time: O(n), space: O(1)
        n = len(nums)
        if n < 4: 
            return max(nums)
        
        pre2_A = nums[0]
        pre1_A = nums[0]  
        
        pre2_B = 0
        pre1_B = nums[1]
        
        for i in range(2, n):
            if i == n - 1:
                cur_A = pre1_A
            else:
                cur_A = max(pre1_A, pre2_A + nums[i])
                
            cur_B = max(pre1_B, pre2_B + nums[i])
            
            pre2_A, pre1_A = pre1_A, cur_A
            pre2_B, pre1_B = pre1_B, cur_B
            
        return max(pre1_A, pre1_B)