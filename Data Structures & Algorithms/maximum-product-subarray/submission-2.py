class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = [1] * (len(nums) + 1)
        sufix = [1] * (len(nums) + 1)
        res = float('-inf')

        for i in range(1, len(nums) + 1):
            last_prefix = 1 if prefix[i - 1] == 0 else prefix[i - 1]
            prefix[i] = last_prefix * nums[i - 1]

            last_sufix = 1 if sufix[i - 1] == 0 else sufix[i - 1]                
            sufix[i] *= last_sufix * nums[len(nums) - i]
            
            res = max(res, prefix[i], sufix[i])

        return res



# prefix
# 1, 2, -3, 4
# [1, 1, 2, -6, -24]
# sufix
# 4, -3, 2, 1
# [1, 4, -12, -24, -24]
