class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        prev = 1

        for _ in range(n - 1):
            prev, curr = curr, curr + prev
        
        return curr