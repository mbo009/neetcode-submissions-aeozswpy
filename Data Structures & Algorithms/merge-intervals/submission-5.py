class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals[1:]:
            print(interval)
            if end < interval[0]:
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                start = min(interval[0], start)
                end = max(interval[1], end)
        
        if len(merged) == 0 or merged[-1] != [start, end]:
            merged.append([start, end])
        
        return merged