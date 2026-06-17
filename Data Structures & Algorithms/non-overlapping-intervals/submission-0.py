class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy

        intervals.sort() #O(nlogn)
        count = 0
        cur = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < cur:
                count += 1
                cur = min(cur, intervals[i][1])
            else:
                cur = intervals[i][1]
                
        return count