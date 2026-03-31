from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
            
        safe = set()

        for i in range(len(board)):
            if board[i][0] == "O":
                safe.add((i, 0))
            if board[i][len(board[0]) - 1] == "O":
                safe.add((i, len(board[0]) - 1))
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                safe.add((0, i))
            if board[len(board) - 1][i] == "O":
                safe.add((len(board) - 1, i))
        
        queue = deque(list(safe))

        while queue:
            i, j = queue.popleft()

            for si, sj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i = i + si
                new_j = j + sj

                if new_i < 0 or new_j < 0 or new_i >= len(board) or new_j >= len(board[0]):
                    continue
                if (new_i, new_j) in safe or board[new_i][new_j] != "O":
                    continue
                safe.add((new_i, new_j))
                queue.append((new_i, new_j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"