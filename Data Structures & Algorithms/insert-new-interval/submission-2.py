class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        
        found = i
        start = newInterval[0]
        end = newInterval[1]

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
                
        return intervals[:found] + [[start, end]] + intervals[i:]