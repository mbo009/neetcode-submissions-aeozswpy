from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        next_max = deque()
        queue = deque()
        res = []

        for i in range(len(nums)):
            while len(next_max) > 0 and nums[i] > next_max[-1]:
                next_max.pop()

            queue.append(nums[i])
            next_max.append(nums[i])

            if len(queue) > k:
                val_out = queue.popleft()
                if val_out == next_max[0]:
                    next_max.popleft()
            
            if len(queue) == k:
                res.append(next_max[0])  
          
        return res
