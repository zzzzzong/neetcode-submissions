import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for char in nums:
            if char not in hmap:
                hmap[char] = 1
                continue
            hmap[char] += 1

        min_heap = []
        
        for key in hmap:
            heapq.heappush(min_heap, (hmap[key], key))
            if len(min_heap) == k + 1:
                heapq.heappop(min_heap)
        
        ans = [i[1] for i in min_heap]

        return ans