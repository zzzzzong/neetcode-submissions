class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        res = 0

        for i in check:
            count = 1
            cur = i
            while cur - 1 in check:
                cur -= 1
                count += 1
            res = max(res, count)
        
        return res