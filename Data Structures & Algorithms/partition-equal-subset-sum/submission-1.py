class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(sum1, sum2, idx):
            if idx == len(nums):
                return sum1 == sum2
    
            add = nums[idx]

            return dfs(sum1 + add, sum2, idx + 1) or dfs(sum1, sum2 + add, idx + 1)

        return dfs(0, 0, 0)
