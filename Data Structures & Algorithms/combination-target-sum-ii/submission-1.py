class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack, timeL O(4^n), space: O(n)

        n = len(candidates)
        candidates.sort() # O(nlogn)
        res = []
        cur_val = 0

        def dfs(cur_index: int, cur_arr: list) -> None:
            nonlocal cur_val
            
            # base case
            if cur_val == target:
                res.append(cur_arr[:])
                return
            
            if cur_val > target:
                return
            
            # layer process
            
            tmp_val = -1
            for i in range(cur_index, n):
                if cur_val + candidates[i] > target:
                    break
                if candidates[i] == tmp_val:
                    continue
                tmp_val = candidates[i]
                cur_arr.append(candidates[i])
                cur_val += candidates[i]

                dfs(i + 1, cur_arr)
                
                cur_arr.pop()
                cur_val -= candidates[i]                
            
            return
        
        dfs(0, [])

        return res