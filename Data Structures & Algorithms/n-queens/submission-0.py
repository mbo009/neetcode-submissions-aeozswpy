class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n for _ in range(n)]
        res = []        
        def mark(board, i, j, direction):
            for k in range(1, n - i):
                board[i + k][j] += direction
                
                if j - k >= 0:
                    board[i + k][j - k] += direction
                
                if j + k < n:
                    board[i + k][j + k] += direction
    
        def backtrack(i):
            if i == n:
                solution = []
                for row in board:
                    row_str = ""
                    for field in row:
                        if field == -1:
                            row_str += "Q"
                        else:
                            row_str += "."
                    solution.append(row_str)
                res.append(solution)
                return
                        
            for j in range(n):
                if board[i][j] == 0:
                    mark(board, i, j, 1)
                    board[i][j] = -1
                    backtrack(i + 1)
                    board[i][j] = 0
                    mark(board, i, j, -1)
        
        backtrack(0)
        return res
        
