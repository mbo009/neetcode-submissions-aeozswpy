from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
            in_degree[a] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_count = 0

        while queue:
            curr = queue.popleft()
            visited_count += 1
            
            for neighbor in graph.get(curr, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_count == numCourses


# a->b->c,  d->e

