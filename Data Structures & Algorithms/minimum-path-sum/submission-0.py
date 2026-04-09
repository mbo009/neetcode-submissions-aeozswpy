class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                for mov_i, mov_j in [(i + 1, j), (i, j + 1)]:
                    if mov_i >= m or mov_j >= n:
                        continue
                    
                    dp[mov_i][mov_j] = min(dp[mov_i][mov_j], dp[i][j] + grid[mov_i][mov_j])

        return dp[m - 1][n - 1]