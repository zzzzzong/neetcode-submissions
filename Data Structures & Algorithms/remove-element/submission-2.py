class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers, time: O(n), space: O(1)

        writing_index = 0

        for pivot in range(len(nums)):
            if nums[pivot] != val:
                nums[writing_index] = nums[pivot]
                writing_index += 1

        return writing_index