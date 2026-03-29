class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
            
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue[0]
            del queue[0]

            for shift_y, shift_x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                y = i + shift_y
                x = j + shift_x

                if 0 <= y < len(grid) and \
                   0 <= x < len(grid[0]) and \
                   grid[y][x] == 2147483647:
                    grid[y][x] = grid[i][j] + 1
                    queue.append((y, x))