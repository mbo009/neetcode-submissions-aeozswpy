class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()

        def sum_count(i, curr):    
            if i == len(nums):
                return int(curr == target)
            
            if (i, curr) in memo:
                return memo[(i, curr)]

            add = sum_count(i + 1, curr + nums[i])
            subtract = sum_count(i + 1, curr - nums[i])
            memo[(i, curr)] = add + subtract

            return memo[(i, curr)]
    
        return sum_count(0, 0)