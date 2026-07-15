class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        while i <= j:
            mid = (i + j) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours > h:
                i = mid + 1
            else:
                j = mid - 1
                
        return i