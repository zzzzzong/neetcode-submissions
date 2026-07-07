import heapq

class KthLargest:
    # sorting method, time: O(n * logk), space = O(k) n is the extra space

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # 實務上都是用array來實作heap, 用heapq的heapify method去堆積化array, time: O(n)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # O(logn) -> pop the peak O(1), and sift down O(logn)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(logn) -> append to the leaf O(1), and sift up O(logn)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]