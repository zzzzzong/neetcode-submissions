class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()

        for i in nums:
            if i in check:
                return i
            else:
                check.add(i)