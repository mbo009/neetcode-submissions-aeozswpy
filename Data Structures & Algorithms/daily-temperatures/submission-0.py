from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = deque()

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                pop_temperature, pop_idx = stack.pop()
                res[pop_idx] = i - pop_idx
            stack.append((temperature, i))

        return res
# 2 stack = [0] 
# 1 stack = [0, 1]
# 1 stack = [0, 1, 2]
# 3 stack = [3]

# 2 stack = [3]
# 1
# 1
# 3
