class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        char_set = set()

        for i in nums:
            if i in char_set:
                return True
            else:
                char_set.add(i)
        
        return False