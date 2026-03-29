class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def backtrack(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums):
                return False
            
            res = False
            for j in range(1, nums[i] + 1):
                res |= backtrack(i + j)
            
            return res
        
        return backtrack(0)