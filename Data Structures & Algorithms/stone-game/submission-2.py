class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.memo = {}

        def pick(i, j):
            if i == j:
                return piles[i]

            if (i, j) in self.memo:
                return self.memo[(i, j)]

            left = piles[i] - pick(i + 1, j)
            right = piles[j] - pick(i, j - 1)
            self.memo[(i, j)] = max(left, right)
            return self.memo[(i, j)]

        return pick(0, len(piles) - 1) > 0        
        