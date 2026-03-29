class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_set = set()
        a_set = set()
        temp_set = set()

        def dfs(i, j, prev):
            if i < 0 or i >= len(heights):
                return
            if j < 0 or j >= len(heights[0]):
                return
            if heights[i][j] < prev or (i, j) in temp_set:
                return
            
            temp_set.add((i, j))

            for shift_i, shift_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + shift_i, j + shift_j, heights[i][j])
            
    
        for i in range(len(heights[0])):
            dfs(0, i, -1)
        for i in range(len(heights)):
            dfs(i, 0, -1)
        
        p_set = temp_set
        temp_set = set()

        for i in range(len(heights[0])):
            dfs(len(heights) - 1, i, -1)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, -1)
        
        a_set = temp_set
        return sorted(list(p_set.intersection(a_set)))

        
