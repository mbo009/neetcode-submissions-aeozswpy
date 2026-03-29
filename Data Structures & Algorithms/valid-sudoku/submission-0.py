class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                field = board[i][j]
                if field == ".":
                    continue

                if field in rows[i]:
                    return False
                else:
                    rows[i].add(field)
                
                if field in columns[j]:
                    return False
                else:
                    columns[j].add(field)
                
                square_corner = (i // 3) * 3 + (j // 3)
                if field in squares[square_corner]:
                    return False
                else:
                    squares[square_corner].add(field)
        
        return True

# 1. Columns no duplicates
# 2. Rows no duplicates
# 3. Each 3x3 square no duplicates

# i - rows
# j - columns

# board=[["1","2",".",".","3",".",".",".","."],
#.       ["4",".",".","5",".",".",".",".","."],
#.       [".","9","8",".",".",".",".",".","3"],
#        ["5",".",".",".","6",".",".",".","4"],
#        [".",".",".","8",".","3",".",".","5"],
#        ["7",".",".",".","2",".",".",".","6"],
#        [".",".",".",".",".",".","2",".","."],
#        [".",".",".","4","1","9",".",".","8"],
#        [".",".",".",".","8",".",".","7","9"]]
