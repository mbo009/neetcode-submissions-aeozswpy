from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1

            for prerequisite in graph[course]:
                if dfs(prerequisite):
                    return True
            
            visited[course] = 2
            return False

        for course in range(numCourses):
            if visited[course] == 0:
                if dfs(course):
                    return False
    
        return True