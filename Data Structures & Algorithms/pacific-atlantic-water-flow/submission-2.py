from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        def create_set(sea):
            queue = deque(list(sea))
        
            while queue:
                i, j = queue.popleft()
                for si, sj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i = i + si
                    new_j = j + sj
                    
                    if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]):
                        continue
                    
                    if (new_i, new_j) in sea or heights[new_i][new_j] < heights[i][j]:
                        continue
                    sea.add((new_i, new_j))
                    queue.append((new_i, new_j))
            
            return sea

        pacific = set([(0, i) for i in range(len(heights[0]))])
        pacific.update([(i, 0) for i in range(len(heights))])
        pacific = create_set(pacific)   

        atlantic = set([(len(heights) - 1, i) for i in range(len(heights[0]))])
        atlantic.update([(i, len(heights[0]) - 1) for i in range(len(heights))])
        atlantic = create_set(atlantic)
        
        return [list(x) for x in pacific.intersection(atlantic)]                
                
                
                