class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking x swap, time: O(n * n!), space: O(n)/O(1) if not include return space
        n = len(nums)
        res = []

        def dfs(first: int) -> None:
            if first == n:
                res.append(nums[:])
                return
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        dfs(0)
        return res