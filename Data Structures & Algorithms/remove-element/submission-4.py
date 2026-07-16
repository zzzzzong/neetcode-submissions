class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers(inward shrinking from both left and right), time: O(n), space: O(1)

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        
        return left