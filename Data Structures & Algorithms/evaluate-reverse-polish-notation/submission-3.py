import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": lambda x, y: x + y,
                     "-": lambda x, y: x - y,
                     "*": lambda x, y: x * y,
                     "/": lambda x, y: int(x / y)}

        for token in tokens:
            if operators.get(token, 0) != 0:
                stack[-1] = operators[token](stack[-2], stack[-1])
                del stack[-2]
            else:
                stack.append(int(token))

        return stack[-1]