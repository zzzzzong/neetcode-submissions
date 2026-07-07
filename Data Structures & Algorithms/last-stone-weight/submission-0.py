import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones] # just add a minus sign
        heapq.heapify(max_heap)  # in-place modify, O(n)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            if stone1 != stone2:    # remember, the numbers here are all negative
                heapq.heappush(max_heap, stone1 - stone2)

        return -max_heap[0] if max_heap else 0