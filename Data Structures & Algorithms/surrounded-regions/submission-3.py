class Solution:
    def solve(self, board: List[List[str]]) -> None:
        connected = set()
        queue = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in connected:
                    if i + 1 == len(board) or i - 1 < 0 or j + 1 == len(board[0]) or j - 1 < 0:
                        connected.add((i, j))
                        queue.append((i, j))
                
                while queue:
                    curr_i, curr_j = queue[0]
                    del queue[0]
                    for s_i, s_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        if 0 <= curr_i + s_i < len(board) and 0 <= curr_j + s_j < len(board[0]) and board[curr_i][curr_j] == "O" and (curr_i + s_i, curr_j + s_j) not in connected:
                            connected.add((curr_i + s_i, curr_j + s_j))
                            queue.append((curr_i + s_i, curr_j + s_j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in connected:
                    board[i][j] = "X"
                
