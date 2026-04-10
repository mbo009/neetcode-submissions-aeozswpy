class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.max_profit = 0
        visited = {}

        def profit_rec(i, profit, bought):
            if i >= len(prices):
                self.max_profit = max(self.max_profit, profit)
                return

            key = (i, bought)

            if key in visited:
                if visited[key] >= profit:
                        return
            visited[key] = profit

            if not bought:
                profit_rec(i + 1, profit - prices[i], True)
            else:
                profit_rec(i + 2, profit + prices[i], False)

            profit_rec(i + 1, profit, bought)

        profit_rec(0, 0, False)
        return self.max_profit