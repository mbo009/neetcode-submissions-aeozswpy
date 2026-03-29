class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        sufix = [1] * (len(nums) + 1)

        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] * num
        
        for i, num in enumerate(nums[::-1]):
            sufix[len(nums) - i - 1] = sufix[len(nums) - i] * num
        
        return [curr_p * curr_s for curr_p, curr_s in zip(prefix[:-1], sufix[1:])]

