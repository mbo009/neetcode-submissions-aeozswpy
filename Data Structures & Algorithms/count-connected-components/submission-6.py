class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            parent_i = find(i)
            parent_j = find(j)
            if parent_i != parent_j:
                parent[parent_i] = parent_j
                return 1
            return 0
    
        components = n
        for u, v in edges:
            components -= union(u, v)
        
        return components
