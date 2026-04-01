from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = [False for _ in range(numCourses)]
        checked = [False for _ in range(numCourses)]
        path = deque()

        def dfs(i):
            if visited[i]:
                return True
            if checked[i]:
                return False

            visited[i] = True
            for neighbor in graph[i]:
                if dfs(neighbor):
                    return True
                
            visited[i] = False
            checked[i] = True
            path.appendleft(i)

            return False


        for i in range(numCourses):
            if not checked[i]:
                if dfs(i):
                    return []
        
        return list(path)