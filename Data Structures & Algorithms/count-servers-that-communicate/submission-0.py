class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [0] * len(grid)
        columns = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    columns[j] += 1

        servers = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rows[i] > 1 or columns[j] > 1):
                    servers += 1
                
        return servers