class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for char in nums:
            if char in check:
                return char
            check.add(char)