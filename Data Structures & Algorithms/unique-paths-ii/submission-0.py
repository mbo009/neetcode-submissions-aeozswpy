class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
            
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[n - 1][m - 1]