from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        visited = [False] * numCourses

        def is_cycle(i):
            if visited[i]:
                return True
            
            visited[i] = True

            for neighbor in graph[i]:
                if is_cycle(neighbor):
                    return True
            
            visited[i] = False
            return False
        
        for i in range(numCourses):
            if is_cycle(i):
                return False
        
        return True
