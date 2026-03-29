class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = float('-inf')
        i = 0
        j = len(heights) - 1

        while i < j:
            curr_water = (j - i) * min(heights[i], heights[j])
            curr_max = max(curr_max, curr_water)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return curr_max