class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force, time: O(n), space: O(n)
        res = []

        for char in nums:
            if char == val:
                continue
            res.append(char)

        for i in range(len(res)):
            nums[i] = res[i]
        
        return len(res)