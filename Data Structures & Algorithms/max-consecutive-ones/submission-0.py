class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        curr_len = 0

        for num in nums:
            if num == 1:
                curr_len += 1
            else:
                curr_max = max(curr_max, curr_len)
                curr_len = 0
        
        return max(curr_max, curr_len)