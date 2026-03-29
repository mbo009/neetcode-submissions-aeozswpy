class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged = [sorted_intervals[0]]
        print(sorted_intervals)
        for interval in sorted_intervals[1:]:
            if interval[0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
            else:
                merged.append(interval)

        return merged