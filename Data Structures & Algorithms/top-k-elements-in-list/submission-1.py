from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        res = []

        for i in range(k):
            number = max(hmap, key = hmap.get)
            res.append(number)
            del hmap[number]

        return res