class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(amount + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                coin = coins[j - 1]

                dp[i][j] = dp[i][j - 1]
        
                if i >= coin:
                    dp[i][j] += dp[i - coin][j]

        return dp[amount][n]