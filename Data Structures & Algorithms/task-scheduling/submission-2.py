from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_tasks = Counter(tasks)
        max_heap = [cnt for cnt in count_tasks.values()]
        heapq.heapify_max(max_heap)
        queue = deque()
        cycles = 0

        while max_heap or queue:
            cycles += 1
            
            if max_heap:
                curr = heapq.heappop_max(max_heap)
                if curr - 1 != 0:
                    queue.append((curr - 1, cycles + n))
            
            if queue and queue[0][1] == cycles:
                heapq.heappush_max(max_heap, queue.popleft()[0])

        return cycles