from functools import lru_cache

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.curr_min = float('inf')
        stone_sum = sum(stones)
        perfect = (stone_sum + 1) // 2

        @lru_cache(None)
        def dfs(i, total):
            if total >= perfect:
                self.curr_min = min(self.curr_min, total - (stone_sum - total))
                return
            
            if i >= len(stones):
                return

            dfs(i + 1, total)
            dfs(i + 1, total + stones[i])
        
        dfs(0, 0)

        return self.curr_min

