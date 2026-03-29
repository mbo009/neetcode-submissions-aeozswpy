

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        brackets = {"]": "[",
                    "}": "{",
                    ")": "("}
        stack = []
        
        for bracket in s:
            if len(stack) > 0 and brackets.get(bracket, 0) != 0:
                if stack[-1] != brackets[bracket]:
                    return False
                else:
                    del stack[-1]
            else:
                stack.append(bracket)
        
        return len(stack) == 0
            