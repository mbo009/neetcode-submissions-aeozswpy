class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x: x[1])
        res = 0
        prev = sorted_intervals[0]

        for interval in sorted_intervals[1:]:
            if prev[1] > interval[0]:
                res += 1
            else:
                prev = interval
        
        return res


# [1, 2], [1, 4], [2, 4]
#  1  
