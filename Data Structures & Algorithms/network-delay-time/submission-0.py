from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append([time[2], time[1]])
        
        distances = [float('inf') for _ in range(n + 1)]
        distances[k] = 0
        queue = [[0, k]]
        heapq.heapify(queue) 

        while queue:
            curr = heapq.heappop(queue)
            if curr[0] > distances[curr[1]]:
                continue
            
            for node in graph[curr[1]]:
                if curr[0] + node[0] < distances[node[1]]:
                    distances[node[1]] = curr[0] + node[0]
                    heapq.heappush(queue, [curr[0] + node[0], node[1]])
        
        res = max(distances[1:])
        return res if res != float('inf') else -1