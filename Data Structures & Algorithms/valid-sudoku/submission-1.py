class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_lines(curr_board):
            for row in curr_board:
                curr_set = set()
                
                for num in row:
                    if num == ".":
                        continue

                    if num in curr_set:
                        return False

                    curr_set.add(num)
            
            return True
    
        def check_squares():
            for row in range(0, 9, 3):
                for column in range(0, 9, 3):
                    curr_set = set()

                    for i in range(row, row + 3):
                        for j in range(column, column + 3):
                            num = board[i][j]

                            if num == ".":
                                continue

                            if num in curr_set:
                                return False

                            curr_set.add(num)
            return True                        
                        
        return check_lines(board) and check_lines(zip(*board)) and check_squares()
        

