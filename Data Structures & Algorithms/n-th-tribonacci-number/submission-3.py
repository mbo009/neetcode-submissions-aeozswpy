from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        t = deque([0, 1, 1])
        curr_sum = 2
    
        for i in range(3, n):
            t.append(curr_sum)
            curr_sum -= t.popleft()
            curr_sum += t[-1]
        
        return curr_sum


