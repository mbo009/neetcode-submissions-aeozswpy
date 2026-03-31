class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(i, j, distance):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] < distance:
                return
            
            grid[i][j] = distance
            for si, sj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + si, j + sj, distance + 1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
        