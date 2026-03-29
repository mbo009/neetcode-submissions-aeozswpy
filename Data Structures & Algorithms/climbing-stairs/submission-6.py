class Solution:
    def climbStairs(self, n: int) -> int:
        short = 1
        long = 1

        for _ in range(n - 1):
            long, short = short + long, long
        
        return long