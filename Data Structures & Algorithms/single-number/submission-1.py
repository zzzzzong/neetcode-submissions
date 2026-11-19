class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = set()

        for char in nums:
            if char not in check:
                check.add(char)
                continue
            check.discard(char)
        
        return list(check)[0]