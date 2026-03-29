class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = -1
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            
            return 0

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area


        

# we iterate through graph, if we find 1 we do dfs to mark it with # and count it,
# if we find 0, and # we are skipping this node.

