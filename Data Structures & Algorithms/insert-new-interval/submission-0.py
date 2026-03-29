class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        
        res.append(newInterval)
        if i < len(intervals):
            return res + intervals[i:]
    
        return res





# linear:
# 1. whole interval before everything
# 2. merge
# 3. whole interval after everything

# newInterval = [0, 1]
# intervals = [2, 3], [4, 5]
# [0, 1], [2, 3], [4, 5]

# newInterval = [2, 6]
# intervals = [2, 3], [4, 5]
# [2, 6]

# newInterval = [5, 7]
# intervals = [2, 3], [4, 5]
# [2, 3], [4, 7]

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
#     - -  
#         - -
#             - - -
#           - - -
# 
