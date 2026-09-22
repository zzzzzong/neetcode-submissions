class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        [ intuition ]

        1. Sort intervals and queries to use a two-pointer approach (moving forward only).
        2. Use a Min-Heap to dynamically store valid intervals, sorted by their length.
        3. Pop "expired" intervals (right bound < q) from the heap.
        4. The top of the heap is always the smallest valid interval for the current query.
        '''
        intervals.sort()
        
        # 1. 將 (query, original_index) 綁在一起排序，確保排序後還能找回原本的答案位置
        sorted_queries = sorted((q, index) for index, q in enumerate(queries))

        hmap = {}      # 用來記錄原本索引位置 (original_index) 所對應的最小長度答案
        min_heap = []  # 最小堆疊，存放格式為: (區間長度, 區間右界)
        i = 0          # 雙指標：用來記錄目前處理到 intervals 的哪一個位置
        n = len(intervals)

        # 2. 開始遍歷排序後的 queries
        for q, original_index in sorted_queries:
            
            # 第一步：把所有「左界符合條件 (<= q)」的區間通通塞進 Heap，指標 i 一路向右不回頭
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i][0], intervals[i][1]
                length = right - left + 1
                heapq.heappush(min_heap, (length, right)) # 依據長度自動排序
                i += 1
            
            # 第二步：從 Heap 頂端剔除「右界已經過期 (< q)」的區間
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # 第三步：此時 Heap 頂端就是我們要的最優解
            if min_heap:
                hmap[original_index] = min_heap[0][0] # 紀錄此原索引的答案為 Heap 頂端的長度
            else:
                hmap[original_index] = -1

        # 3. 按照原本 queries 的順序，把答案填入 ans 陣列中
        ans = []
        for index in range(len(queries)):
            ans.append(hmap[index])

        return ans