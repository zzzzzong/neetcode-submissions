class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_conn = 0
        s = set(nums)

        for i in s:
            conn = 1
            while i - 1 in s:
                conn += 1
                i -= 1
            max_conn = max(max_conn, conn)
        
        return max_conn