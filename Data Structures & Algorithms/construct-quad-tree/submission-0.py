"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def rec_box(i, j, size):
            if size == 1:
                return Node(grid[i][j], 1)
            
            base_value = grid[i][j]
            is_uniform = True

            for y in range(i, i + size):
                for x in range(j, j + size):
                    if grid[y][x] != base_value:
                        is_uniform = False
                        break
                if not is_uniform:
                    break
            
            if is_uniform:
                return Node(base_value, 1)
            
            new_size = size // 2
            top_left = rec_box(i, j, new_size)
            top_right = rec_box(i, j + new_size, new_size)
            bottom_left = rec_box(i + new_size, j, new_size)
            bottom_right = rec_box(i + new_size, j + new_size, new_size)
            
            return Node(1, 0, top_left, top_right, bottom_left, bottom_right)

        return rec_box(0, 0, len(grid))
