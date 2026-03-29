from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        res = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                alive = True
                while stack and stack[-1] <= abs(asteroid):
                    last = stack.pop()
                    if last == abs(asteroid):
                        alive = False
                        break
                
                if alive and not stack:
                    res.append(asteroid)
        
        return res + list(stack)