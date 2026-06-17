class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        char_set = set(nums)

        for i in char_set:
            if i - 1 not in char_set:
                count = 1
                while i + count in char_set:
                    count += 1
                    
                res = max(res, count)
        
        return res