class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        sufix = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            sufix[i] = sufix[i + 1] * nums[i + 1]
        
        print(prefix, sufix)
        return [prefix[i] * sufix[i] for i in range(len(nums))]



#   1 2 3 4 5
# prod_value = 0
# 1. prefix = 1
# 2. prefix = 1
# 3. prefix = 2
# 4. prefix = 6
# 5. prefix = 24

# 5. prefix = 1
# 4. prefix = 5
# 3. prefix = 20
# 2. prefix = 60
# 1. prefix = 120

# 1. -, 2, 3, 4, 5
# 2. 1, -, 3, 4, 5
# 3. 1, 2, -, 4, 5
# 4. 1, 2, 3, -, 5
# 5. 1, 2, 3, 4, -
