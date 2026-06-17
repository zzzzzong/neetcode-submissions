class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        n = len(nums)

        nums.sort() # O(nlogn)
        
        def dfs(idx: int, cur_combi: list[int], rest: int) -> None:
            if rest == 0:
                self.res.append(cur_combi[:])
                return
            
            if rest < 0:
                return
            
            for i in range(idx, n):
                cur_combi.append(nums[i])
                dfs(i, cur_combi, rest - nums[i])
                cur_combi.pop()
            
            return

        dfs(0, [], target)
        return self.res