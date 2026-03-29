class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def two_sum(start, target):
            left = start
            right = len(nums) - 1
            two_sums = []

            while left < right:
                curr_sum = nums[left] + nums[right]                
                if curr_sum == target:
                    two_sums.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
                    
            return two_sums
        
        three_sums = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            three_sums.extend(two_sum(i + 1, -nums[i]))
    
        return three_sums



