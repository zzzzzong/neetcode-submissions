import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counter + time stamp + max heap
        # time: O()
        # space: O()

        # count the tasks
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        
        # initialize the (1)max heap, (2)queue, (3)time stamp
        max_heap = [-c for c in counts if c > 0]
        heapq.heapify(max_heap)                                # O(n)
        queue = deque()
        time = 0
        
        while max_heap or queue:
            time += 1
            
            if max_heap:
                c = heapq.heappop(max_heap) + 1                # O(logn)
                if c < 0:
                    queue.append((c, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])    # O(logn)
                
        return time

