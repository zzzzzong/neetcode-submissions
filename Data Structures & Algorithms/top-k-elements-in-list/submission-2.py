class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for j in range(k):
            top = max(hashmap, key = hashmap.get)
            res.append(top)
            del hashmap[top]
        
        return res