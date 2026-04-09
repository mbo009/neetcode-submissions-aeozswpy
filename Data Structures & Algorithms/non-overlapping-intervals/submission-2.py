class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prev_end = float('-inf')
        count = 0

        for start, end in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end
        
        return len(intervals) - count



# [[1,2],[2,4],[1,4]]
