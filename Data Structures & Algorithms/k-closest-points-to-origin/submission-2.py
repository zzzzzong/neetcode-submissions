import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap(space optimized), time O(nlogn) because k <= n, space: O(n)

        max_heap = []
        for p in points:                        # O(n)
            distance = p[0] ** 2 + p[1] ** 2
            heapq.heappush(max_heap, (-distance, p)) # O(logn)

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        
        res = []                                # O(k)
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])  # O(logk)

        return res