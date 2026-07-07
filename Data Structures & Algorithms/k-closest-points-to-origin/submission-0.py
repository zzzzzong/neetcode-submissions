import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            distance = p[0] ** 2 + p[1] ** 2
            heapq.heappush(heap, (distance, p))

        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res