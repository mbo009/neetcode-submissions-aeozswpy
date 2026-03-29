"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prev = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            if prev.end > interval.start:
                return False
            prev = interval
        
        return True

            