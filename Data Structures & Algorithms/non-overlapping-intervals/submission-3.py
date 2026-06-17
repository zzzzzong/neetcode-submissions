class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[1]) #O(nlogn)
        count = 0

        cur_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_end:
                count += 1
            else:
                cur_end = intervals[i][1]
        
        return count