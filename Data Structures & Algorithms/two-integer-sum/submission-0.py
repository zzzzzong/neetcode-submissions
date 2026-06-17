class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashmap:
                return [hashmap[pair], i]
            hashmap[nums[i]] = i
            