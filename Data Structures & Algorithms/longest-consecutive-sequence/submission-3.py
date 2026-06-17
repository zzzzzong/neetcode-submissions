class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        char_set = set(nums)

        for i in char_set:
            if i - 1 not in char_set:
                tmp_count = 1
                while i + tmp_count in char_set:
                    tmp_count += 1
                    
                res = max(res, tmp_count)
        
        return res