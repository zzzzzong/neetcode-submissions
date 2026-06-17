class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hmap:
                return [hmap[pair], i]
            else:
                hmap[nums[i]] = i