class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
    
        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            u_parent = find(u)
            v_parent = find(v)

            if u_parent != v_parent:
                parent[u_parent] = v_parent
                return False

            return True

        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return []