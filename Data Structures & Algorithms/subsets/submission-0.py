class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(cur_list: list, cur_index: int) -> list[list[int]]:
            if cur_index == n:
                res.append(cur_list)
                return
            
            # 2. 核心決策：分出兩條路
            
            # 選擇一：不要取當前數字，直接看下一個
            dfs(cur_list, cur_index + 1)
            
            # 選擇二：要取當前數字，加進去後看下一個
            dfs(cur_list + [nums[cur_index]], cur_index + 1)

        # 從空列表 [] 和第 0 個位置開始深入
        dfs([], 0)

        return res