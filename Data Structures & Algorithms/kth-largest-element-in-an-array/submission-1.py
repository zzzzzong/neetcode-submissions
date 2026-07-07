import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap, time: O(nlogn), space: O(k)
        
        max_heap = [-x for x in nums] # O(n)
        heapq.heapify(max_heap)       # O(n)
        
        for _ in range(k - 1):        # O(n)
            heapq.heappop(max_heap)   # O(logn)
            
        return -heapq.heappop(max_heap)