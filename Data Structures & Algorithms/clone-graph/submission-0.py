"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = [node]
        old_to_new = {node: Node(node.val)}

        while queue:
            curr = queue[0]
            del queue[0]

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
            
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]

            