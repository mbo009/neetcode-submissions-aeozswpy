class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res            


# 0 + 1 + 2 + 3 = 6
# 1.5 * 4
