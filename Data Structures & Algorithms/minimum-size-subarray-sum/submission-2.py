class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        i = 0
        j = 0
        curr_sum = 0
        min_len = float('inf')
    
        while j < len(nums) or curr_sum >= target:
            if curr_sum >= target:
                curr_sum -= nums[i]
                min_len = min(min_len, j - i)
                i += 1
            else:
                curr_sum += nums[j]
                j += 1
        
        return min_len if min_len != float('inf') else 0
                

# [2, 1, 5, 1, 5, 3]
# i = 0, j = 4, len = 5
# 2, 3, 8, 9, 14 
# i = 1, j = 4, len = 4
# 12

    