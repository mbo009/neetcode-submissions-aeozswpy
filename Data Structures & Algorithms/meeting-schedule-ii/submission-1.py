"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        
        times.sort(key=lambda x: (x[0], x[1]))
        res = 0
        curr = 0
        for time in times:
            curr += time[1]
            res = max(curr, res)
        
        return res



# 0 1 2 3 4 5 6 7 8 9
# - - - - - - - - -
#   - -
#       - -

# brute force: go through every num in range min(intervals), max(intervals):
# count overlaps and return max
