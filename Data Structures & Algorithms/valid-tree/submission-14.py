class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        in_degree = [0] * n
        graph = dict()
        sorted_edges = sorted(edges)
        for edge1, edge2 in sorted_edges:
            smaller = edge1 if edge1 < edge2 else edge2
            bigger = edge1 if edge1 >= edge2 else edge2

            if smaller not in graph:
                graph[smaller] = []
                if bigger in graph:
                    graph[bigger].append(smaller)
                    in_degree[smaller] += 1
                else:
                    graph[bigger] = []
                    graph[smaller].append(bigger)
                    in_degree[bigger] += 1

            elif bigger not in graph:
                graph[bigger] = []
                if smaller in graph:
                    graph[smaller].append(bigger)
                    in_degree[bigger] += 1
                else:
                    graph[smaller] = []
                    graph[bigger].append(smaller)
                    in_degree[smaller] += 1
            
            else:
                print("FALLBACK")
                return False
            print(graph, in_degree)
            
        zero_count = 0
        one_count = 0
        for value in in_degree:
            if value == 0:
                zero_count += 1
            elif value == 1:
                one_count += 1
        
        return n == (zero_count + one_count) and zero_count == 1


# If we want the tree to be valid, we can't have:
# 1. We can't have cycle
# 2. All nodes in the graph should be connected
# 
# In in_degree we should only have one 0
# All other values should be one

# edges=[[0,1],[1,3],[3,2],[1,4]]
# 1. graph = {0: [1], 1: []}
# 2. graph = {0: [1], 1: [3], 3: []}
# 2. graph = {0: [1], 1: [3], 3: [2]}
