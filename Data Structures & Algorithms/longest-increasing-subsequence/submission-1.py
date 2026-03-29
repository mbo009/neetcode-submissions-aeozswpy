class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]

        for num in nums[1:]:
            i = 0
            while i < len(stack) and num > stack[i]:
                i += 1

            if i == len(stack):
                stack.append(num)
            else:
                stack[i] = num
        
        return len(stack)


# 9,1,4,2,3,3,7
# 1 stack = 9           smaller
# 4 stack = 1           bigger 
# 2 stack = 1, 4        bigger
# 3 stack = 1, 2        bigger
# 3 stack = 1, 2, 3     bigger
# 7 stack = 1, 2, 3, 7       