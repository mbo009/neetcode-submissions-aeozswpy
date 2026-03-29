class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtracking(i, j, word_idx):
            if word_idx >= len(word):
                return True

            if (i < 0 or i >= len(board) or 
                j < 0 or j >= len(board[0]) or 
                board[i][j] != word[word_idx]):
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = backtracking(i - 1, j, word_idx + 1) or \
                    backtracking(i + 1, j, word_idx + 1) or \
                    backtracking(i, j - 1, word_idx + 1) or \
                    backtracking(i, j + 1, word_idx + 1)
            
            board[i][j] = temp
            return found
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i, j, 0):
                    return True
        
        return False
