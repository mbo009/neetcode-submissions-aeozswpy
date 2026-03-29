import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while low <= high:
            mid = (low + high) // 2
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / mid)
            
            if curr_h <= h:
                high = mid - 1
                res = mid
            else:
                low = mid + 1
            
        return res



# 1, 4, 3, 2
# brute force: for min(piles) -> max(piles): calculate curr_h
# Optimal: instead of doing len_step = 1, we perform binary search
# low = 1, high = max(piles), mid = (low + high) // 2
# we calculate curr_h for mid
# if we get curr_h <= h we need to shift high pointer to mid - 1 and save mid.
# if we get that curr_h > h: we shift left pointer to mid + 1