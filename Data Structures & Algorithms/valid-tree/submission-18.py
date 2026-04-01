from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        visited = set()
        queue = deque([(0, -1)])
        prev = None

        while queue:
            curr, parent = queue.popleft()

            if curr in visited:
                return False

            for child in graph[curr]:
                if child != parent:
                    queue.append((child, curr))

            prev = curr
            visited.add(curr)
        
        return len(visited) == n