class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Core Logic:
        1. Identify which half (left or right) is sorted/increasing.
        2. Check if target lies within that sorted range to narrow the search.
        '''

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                    continue
                left = mid + 1

                continue
            
            if nums[mid] < target <= nums[right]:
                left = mid + 1
                continue
            right = mid - 1
        
        return -1