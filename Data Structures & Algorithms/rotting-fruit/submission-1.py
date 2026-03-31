from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2)
        changes = 1
        minutes = 0

        while changes != 0:
            changes = 0
            new_queue = deque()

            while len(queue) > 0:
                i, j = queue.popleft()

                for si, sj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    n_i = i + si
                    n_j = j + sj

                    if n_i < 0 or n_i >= len(grid) or n_j < 0 or n_j >= len(grid[0]):
                        continue

                    if grid[n_i][n_j] == 1:
                        grid[n_i][n_j] = 2
                        changes += 1
                        new_queue.append((n_i, n_j))

            queue = new_queue
            minutes += 1
        
        if any(grid[i][j] == 1 for i in range(len(grid)) for j in range(len(grid[0]))):
            return -1
            
        return minutes - 1

