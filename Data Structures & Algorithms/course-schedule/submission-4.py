from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        visited = [False] * numCourses
        safe = [False] * numCourses

        def is_cycle(i):
            if visited[i]:
                return True
            if safe[i]:
                return False
            
            visited[i] = True

            for neighbor in graph[i]:
                if is_cycle(neighbor):
                    return True
            
            visited[i] = False
            safe[i] = True
            return False
        
        for i in range(numCourses):
            if not safe[i]:
                if is_cycle(i):
                    return False
        
        return True
