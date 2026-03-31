class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.curr_count = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return

            if grid[i][j] != 1:
                return

            grid[i][j] = -1
            self.curr_count += 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + di, j + dj)
             
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    max_area = max(max_area, self.curr_count)
                    self.curr_count = 0
        
        return max_area
