from collections import defaultdict, deque

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node, parent):
            total_time = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                time_from_child = dfs(neighbor, node)                
                if time_from_child > 0 or hasApple[neighbor]:
                    total_time += time_from_child + 2
            
            return total_time

        return dfs(0, -1)
                    

