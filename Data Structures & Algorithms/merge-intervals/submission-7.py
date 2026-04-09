class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        start, end = intervals[0]

        for s, e in intervals[1:]:
            if s > end:
                merged.append([start, end])
                start, end = s, e
            else:
                end = max(end, e)

        merged.append([start, end])
        return merged