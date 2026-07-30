class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        sufix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]
            sufix[i + 1] = sufix[i] * nums[len(nums) - i - 1]
        
        print(prefix, sufix)
        return [n1 * n2 for n1, n2 in zip(prefix[:-1], sufix[:-1][::-1])]