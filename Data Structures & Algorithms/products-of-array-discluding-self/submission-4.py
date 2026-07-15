class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        sufix = [1]

        for num in nums:
            prefix.append(num * prefix[-1])
        
        for num in nums[::-1]:
            sufix.append(num * sufix[-1])
        
        prefix = prefix[:-1]
        sufix = sufix[:-1][::-1]
        output = []

        for i in range(len(prefix)):
            output.append(prefix[i] * sufix[i])

        return output