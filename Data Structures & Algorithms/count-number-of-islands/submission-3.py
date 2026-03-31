from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        count = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return

            if grid[i][j] != "1":
                return

            grid[i][j] = "#"

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + di, j + dj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count
                            