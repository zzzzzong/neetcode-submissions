class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        min_val located right next to the gap
        so we just need to find the gap.

        core logic: 
        1. discard the sorted part
        2. number on the right of the gap must be smaller than number on the left of the gap. 
        '''

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
                continue
            right = mid

        return nums[left]