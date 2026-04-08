class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1
                
        start = newInterval[0]
        end = newInterval[1]

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
                
        return new_intervals + [[start, end]] + intervals[i:]