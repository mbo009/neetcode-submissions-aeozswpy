import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(n + 1)}
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        queue = [(0, k)]
        distances = {}

        while queue:
            time, node = heapq.heappop(queue)

            if node in distances:
                continue
            
            distances[node] = time
            
            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(queue, (time + weight, neighbor))

        if len(distances) != n:
            return -1
            
        return max(distances.values())