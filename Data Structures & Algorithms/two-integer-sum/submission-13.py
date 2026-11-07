class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        n = len(nums)

        for i in range(n):
            pair = target - nums[i]
            if pair in hmap:
                return [hmap[pair], i]
            hmap[nums[i]] = i
        