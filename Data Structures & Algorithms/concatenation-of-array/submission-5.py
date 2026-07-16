class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # time: O(n), space: O(1)
        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
            
        return ans