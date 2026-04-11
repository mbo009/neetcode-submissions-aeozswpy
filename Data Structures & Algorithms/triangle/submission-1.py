class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = dict()

        def dfs(i, j):
            if i >= len(triangle):
                return 0
            
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            
            left = dfs(i + 1, j)
            right = dfs(i + 1, j + 1)
            
            self.memo[(i, j)] = min(left, right) + triangle[i][j]
            return self.memo[(i, j)]
            
        return dfs(0, 0)