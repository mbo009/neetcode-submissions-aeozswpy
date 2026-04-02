from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)
        self.min_coins = float('inf')
        memo = {}

        def dfs(i, remaining, used):
            state = (i, remaining)
            
            if state in memo and memo[state] <= used:
                return
            
            memo[state] = used
            
            if i >= len(coins) or used >= self.min_coins:
                return
            
            new_remaining = remaining - coins[i]
            
            if new_remaining == 0:
                self.min_coins = min(used + 1, self.min_coins)
                return
            
            if new_remaining > 0:
                dfs(i, new_remaining, used + 1)
            
            dfs(i + 1, remaining, used)
        
        dfs(0, amount, 0)
        return self.min_coins if self.min_coins != float('inf') else -1