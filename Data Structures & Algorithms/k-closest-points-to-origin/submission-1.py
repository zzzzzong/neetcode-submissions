import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap, time O(nlogn) because k <= n, space: O(n)
        
        heap = []
        for p in points:                        # O(n)
            distance = p[0] ** 2 + p[1] ** 2
            heapq.heappush(heap, (distance, p)) # O(logn)

        
        res = []                                # O(k)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])  # O(logk)

        return res