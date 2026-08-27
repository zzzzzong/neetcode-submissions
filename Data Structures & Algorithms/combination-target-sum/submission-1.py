class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # O(nlogn)
        n = len(nums)
        res = []

        def dfs(arr: list, cur_sum: int, index: int) -> None:
            if cur_sum == target:
                res.append(arr[:])
                return
            
            for i in range(index, n):
                if cur_sum + nums[i] > target:
                    break
                
                else:
                    arr.append(nums[i])
                    dfs(arr, cur_sum + nums[i], i)
                    arr.pop()
            
            return


        dfs([], 0, 0)

        return res
