class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")" : "(", "}" : "{", "]": "["}
        stack = deque()

        for bracket in s:
            if len(stack) > 0 and stack[-1] == closing.get(bracket, 0):
                stack.pop()
            else:
                stack.append(bracket)
        
        return len(stack) == 0