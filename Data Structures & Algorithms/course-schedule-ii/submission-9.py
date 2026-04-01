class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)
            
        state = [0] * numCourses
        res = []
        
        def dfs(u):
            if state[u] == 1: return False
            if state[u] == 2: return True
            
            state[u] = 1
            for v in adj[u]:
                if not dfs(v): return False
            
            state[u] = 2
            res.append(u)
            return True
            
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i): return []
                
        return res[::-1]