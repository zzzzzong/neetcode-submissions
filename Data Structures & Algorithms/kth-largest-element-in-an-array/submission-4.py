import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap(two loop), time: O(nlogn), space: O(k)

        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap, nums[i])  # O(log k)

        for j in range(k, len(nums)):
            if nums[j] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[j])
        
        return min_heap[0]  # because it's min heap, so the first one is the kth largest