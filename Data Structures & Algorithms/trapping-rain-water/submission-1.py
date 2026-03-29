class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        curr_water = 0
        max_idx = height.index(max(height))
        
        left_max = 0
        for i in range(max_idx):
            if height[i] > left_max:
                left_max = height[i]
            else:
                curr_water += left_max - height[i]
                
        right_max = 0
        for i in range(n - 1, max_idx, -1):
            if height[i] > right_max:
                right_max = height[i]
            else:
                curr_water += right_max - height[i]
                
        return curr_water
# curr_water = 0, prev = None
# h[i] = 0, h[j] = 1, prev = None
# h[i] = 1, h[j] = 1, prev = 0
# curr_water += min(h[i], h[j]) - prev
# curr_water = 1, prev = 1
# h[i] = 1, h[j] = 3, prev = 1
# h[i] = 3, h[j] = 3, prev = 1
# distance = 3, 
