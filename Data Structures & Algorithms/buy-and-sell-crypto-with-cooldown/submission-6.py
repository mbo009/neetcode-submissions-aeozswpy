class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * (len(prices) + 2) for _ in range(2)]

        for i in range(len(prices) - 1, -1, -1):
            dp[1][i] = max(dp[1][i + 1], prices[i] + dp[0][i + 2])
            dp[0][i] = max(dp[0][i + 1], dp[1][i + 1] - prices[i])
        
        return dp[0][0]