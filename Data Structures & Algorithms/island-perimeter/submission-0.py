class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            nonlocal perimeter
            grid[i][j] = -1
            
            for shift_i, shift_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + shift_i, j + shift_j
                
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                    perimeter += 1
                elif grid[ni][nj] == 1:
                    dfs(ni, nj)
        
        start_node = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_node = (r, c)
                    break
            if start_node:
                break
        
        if not start_node:
            return 0

        dfs(start_node[0], start_node[1])
        return perimeter