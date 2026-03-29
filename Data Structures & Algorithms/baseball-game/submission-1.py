from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()

        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))

        return sum(stack)




# 1, 2, +, C, 5, D
# 1