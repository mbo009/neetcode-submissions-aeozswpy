class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
    
        if fresh_count == 0:
            return 0
        
        minutes = 0
        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                i, j = queue[0]
                del queue[0]

                for shift_i, shift_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i = i + shift_i
                    new_j = j + shift_j
                    if 0 <= new_i < len(grid) and \
                    0 <= new_j < len(grid[0]) and \
                    grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh_count -= 1
                        queue.append((new_i, new_j))


        return minutes if fresh_count == 0 else -1