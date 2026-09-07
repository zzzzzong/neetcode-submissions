class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1D-dp(bottom-up), time: O(n * target), space: O(target)
        '''
        [ intuition ]
        Try to find if there's a combination could be made into half of sum of array
        '''

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        # the index is what we try to make into. 
        #   e.g. If I can make the sum == 5, then dp[5] should be True.

        dp = [True] + [False] * target  # length == target + 1
        
        for cur_number in nums:
            for index in range(target, cur_number - 1, -1):
                if dp[index - cur_number]:
                    dp[index] = True

                    if index == target:
                        return True
                    
        return dp[target]