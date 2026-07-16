class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cur = nums[0]
        count = 0

        for i in range(len(nums)):
            if nums[i] == cur:
                count += 1
            else:
                if not count:
                    cur = nums[i]
                else:
                    count -= 1
        
        return cur