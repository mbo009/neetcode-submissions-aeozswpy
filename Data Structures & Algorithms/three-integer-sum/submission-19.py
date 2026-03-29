class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        target = 0
        three_sums = []

        if sorted_nums[0] + sorted_nums[1] + sorted_nums[2] > target:
            return []
        if sorted_nums[-1] + sorted_nums[-2] + sorted_nums[-3] < target:
            return []
        
        def twoSum(i, target):
            if i >= len(nums):
                return []
            two_sums = []
            j = len(nums) - 1

            while i < j:
                curr_sum = sorted_nums[i] + sorted_nums[j]
                if curr_sum == target:
                    two_sums.append([sorted_nums[i], sorted_nums[j]])
                    i += 1
                    j -= 1
                    while i < j and sorted_nums[i] == sorted_nums[i - 1]:
                        i += 1
                elif curr_sum < target:
                    i += 1
                else:
                    j -= 1
            
            return two_sums

        i = 0
        while i < len(nums):
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]:
                i += 1
                continue
    
            two_sum = twoSum(i + 1, target - sorted_nums[i])

            for pair in two_sum:
                three_sums.append(pair + [sorted_nums[i]])
    
            i += 1

        return three_sums

# Solution:
# 1. Sort the nums array
# 2. Pruning to get rid of unnecessary calculations
