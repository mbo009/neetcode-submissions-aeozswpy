class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if max(nums) != len(nums):
            return len(nums)
        
        target = (len(nums) + 1) * max(nums) // 2
        return target - sum(nums)
            


# 0 + 1 + 2 + 3 = 6
# 1.5 * 4
