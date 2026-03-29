class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))

        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parent[root_u] = root_v
                return False
            
            return True

        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return []