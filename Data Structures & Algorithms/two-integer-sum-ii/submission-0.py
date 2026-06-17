class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(numbers)):
            pair = target - numbers[i]
            if pair in hmap:
                return [hmap[pair] + 1, i + 1]
            else:
                hmap[numbers[i]] = i        
        