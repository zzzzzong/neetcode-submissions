class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        a = set(nums)
        ans = 0

        for i in a:
            if i + 1 in a:
                continue
            
            count = 1
            while i - 1 in a:
                count += 1
                i -= 1
            
            if count > ans:
                ans = count
            
        return ans