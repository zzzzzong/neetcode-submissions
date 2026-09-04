class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used_index = set()

        def dfs(arr: list) -> None:
            # base
            if len(arr) == n:
                res.append(arr[:])
                return
            
            # layer logic
            for i in range(n):
                if i in used_index:
                    continue
                
                arr.append(nums[i])
                used_index.add(i)

                dfs(arr)

                arr.pop()
                used_index.discard(i)

        
        dfs([])
        return res