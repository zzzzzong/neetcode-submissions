class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        intuition:
        divide into three conditions:
        -A rob[0: n]
        -B rob[1: n + 1]
        -C rob[1: n]

        so we just need to calculate separately,
        and btw, condition C would be the dp ans before condition B.



        nums[0]    nums[1]    nums[-2]    nums[-1]
        A |----------------------|
        B            |-----------------------|
        C            |-----------|

          |==========|===========|===========|
        '''
        n = len(nums)
        if n < 4:
            return max(nums)
        dp_1, dp_2 = [0] * (n - 1), [0] * (n - 1)

        # case A
        dp_1[0], dp_1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp_1[i] = max(nums[i] + dp_1[i - 2], dp_1[i - 1])
        
        a = dp_1[-1]

        # case B and C
        dp_2[0], dp_2[1] = nums[1], max(nums[1], nums[2])
        b = 0
        c = 0
        for i in range(3, n):
            dp_2[i - 1] = max(nums[i] + dp_2[i - 3], dp_2[i - 2])
            if i == n - 2:
                b = dp_2[i - 1]
            if i == n - 1:
                c = dp_2[i - 1]
        
        return max(a, b, c)