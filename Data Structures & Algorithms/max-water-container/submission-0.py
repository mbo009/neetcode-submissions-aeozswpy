class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = 0

        while i < j:
            water = (j - i) * min(heights[i], heights[j])
            if water > max_water:
                max_water = water

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1 

        return max_water
