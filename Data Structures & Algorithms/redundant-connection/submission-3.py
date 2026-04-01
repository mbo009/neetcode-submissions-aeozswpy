class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(1, len(edges) + 1))
        
        def find(i):
            if parents[i - 1] == i:
                return i
            
            parents[i - 1] = find(parents[i - 1])
            return parents[i - 1]

        def union(u, v):
            root1 = find(u)
            root2 = find(v)

            if root1 != root2:
                parents[root1 - 1] = root2
                return False
            
            return True
        
        excess_edge = None
        for u, v in edges:
            if union(u, v):
                excess_edge = [u, v]
        
        return excess_edge