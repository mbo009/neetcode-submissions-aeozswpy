class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.combinations = 0

        def sum_count(i, curr):
            if i == len(nums):
                if curr == target:
                    self.combinations += 1
                return
            
            sum_count(i + 1, curr + nums[i])
            sum_count(i + 1, curr - nums[i])
        
        sum_count(0, 0)
        return self.combinations