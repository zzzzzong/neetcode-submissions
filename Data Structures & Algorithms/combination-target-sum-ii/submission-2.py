class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtrack, timeL O(4^n), space: O(n)

        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(cur_index: int, target_left: int, cur_arr: list) -> None:
            if target_left == 0:
                res.append(cur_arr[:])
                return
            
            tmp_val = -1
            for i in range(cur_index, n):
                if candidates[i] > target_left:
                    break
                
                if candidates[i] == tmp_val:
                    continue
                
                tmp_val = candidates[i]
                cur_arr.append(candidates[i])
                
                dfs(i + 1, target_left - candidates[i], cur_arr)
                
                cur_arr.pop()
        
        dfs(0, target, [])
        return res