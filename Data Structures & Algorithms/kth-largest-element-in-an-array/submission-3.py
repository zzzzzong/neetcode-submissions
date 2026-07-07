import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap(optimal), time: O(nlogn), space: O(k)

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for char in nums[k:]:
            if char > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, char)
        
        return min_heap[0]  # because it's min heap, so the first one is the kth largest