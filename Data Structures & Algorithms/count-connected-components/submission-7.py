class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        parents = [i for i in range(n)]
        count = n

        def find(i):
            if parents[i] == i:
                return i

            parents[i] = find(parents[i])
            return parents[i]
        
        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1 != root2:
                parents[root1] = root2
                return True
            
            return False

        for parent, child in edges:
            if union(parent, child):
                count -= 1
            
        
        return count
        
