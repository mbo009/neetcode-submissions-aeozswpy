class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            squared_2 = (mid + 1) * (mid + 1)
            if x >= squared and x < squared_2:
                return mid
            if squared > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return 0