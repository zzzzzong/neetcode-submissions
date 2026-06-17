class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}    # key = list.val, val = list.key

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[val] = idx
        
        return []