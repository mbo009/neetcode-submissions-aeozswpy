class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.combinations = 0
        memo = set()

        def sum_count(i, curr):    
            if i == len(nums):
                return int(curr == target)
            
            add = sum_count(i + 1, curr + nums[i])
            subtract = sum_count(i + 1, curr - nums[i])

            return add + subtract
    
        return sum_count(0, 0)