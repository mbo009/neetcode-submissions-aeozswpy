from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        in_degree = [0] * numCourses
        graph = dict()

        for a, b in prerequisites:
            if b not in graph:
                graph[b] = []
            graph[b].append(a)

            in_degree[a] += 1
        
        res = []
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
    
            for neighbor in graph.get(curr, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
           
        return res if len(res) == numCourses else []

        




# Solution:
# 1. Make a graph - show the connections: a : [b]
# 2. Store how many courses depend on course b
# if b is not dependent on any course
# then we can add it to res

# calculus -> math
# algebra -> math
# ai -> comp sci

# math     - 0
# calculus - 1
# algebra  - 2
# comp_sci - 3
# ai       - 4

# graph = {math: [calculus, algebra],
#          comp_sci: [ai]           }

# in_degrees = [0, 1, 1, 0, 1]
# 
# queue where every course on the queue have 0 in_degrees
# pop out of the queue and decrement in_degrees of neighbors
# if it's zero then we add it to res

# graph = {math: [calculus, algebra],
#          comp_sci: [ai],
#          ai: [comp_sci]            }
# in_degrees = [0, 1, 1, 1, 1]

# it work's because we explore the graph with beginning and the cycle is left out



