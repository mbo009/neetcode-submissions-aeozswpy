class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        last = prices[0]
        for price in prices[1:]:
            if price > last:
                profit += price - last
            last = price
    
        return profit



# Solution:
# backtracking
# on each day, we keep track of whether to buy, sell or skip
# if we get to the end we check if it's bigger than previous max

# Solution:
# 