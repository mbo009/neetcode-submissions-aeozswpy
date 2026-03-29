from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for edge, weight in zip(edges, succProb):
            graph[edge[0]].append((weight, edge[1]))
            graph[edge[1]].append((weight, edge[0]))

        max_heap = []
        visited = set()
        distances = [0 for _ in range(n)]
        distances[start_node] = 1
        heapq.heappush_max(max_heap, (1, start_node))

        while max_heap:
            distance, node = heapq.heappop_max(max_heap)
    
            if node == end_node:
                return distance

            if node in visited:
                continue

            visited.add(node)

            for weight, neighbor in graph[node]:
                if neighbor not in visited:
                    new_prob = distance * weight
                    if new_prob > distances[neighbor]:
                        distances[neighbor] = new_prob
                        heapq.heappush_max(max_heap, (distance * weight, neighbor))
        
        return 0.0