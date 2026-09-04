class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort() # O(nlogn)

        def backtrack(cur_index: int, sub_arr: list) -> None:
            if cur_index == n:
                res.append(sub_arr[:])
                return

            sub_arr.append(nums[cur_index])
            backtrack(cur_index + 1, sub_arr)
            sub_arr.pop()

            while cur_index + 1 < n and nums[cur_index] == nums[cur_index + 1]:
                cur_index += 1
            backtrack(cur_index + 1, sub_arr)

        backtrack(0, [])
        return res