class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        sell_price = float('-inf')
        max_profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
                sell_price = price
            if price > sell_price:
                sell_price = price
            
            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

    
# 10, 1, 5, 6, 7, 1
# buy = 10, sell = 10
# buy = 1, sell = 1
