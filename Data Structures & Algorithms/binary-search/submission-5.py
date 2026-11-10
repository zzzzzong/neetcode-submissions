class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            cur = nums[mid]
            if cur == target:
                return mid
            
            if cur < target:
                left = mid + 1
                continue
            right = mid - 1
        
        return -1