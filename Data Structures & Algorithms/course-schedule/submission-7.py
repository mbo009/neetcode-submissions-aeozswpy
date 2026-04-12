from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1
        
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        
        if len(queue) == 0:
            return False
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in graph[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return sum(indegrees) == 0
            