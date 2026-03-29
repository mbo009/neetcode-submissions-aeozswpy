class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def backtrack(i, j):
            if i >= m or j >= n:
                return 0
            if i == (m - 1) and j == (n - 1):
                return 1

            return backtrack(i + 1, j) + backtrack(i, j + 1)

        return backtrack(0, 0) 