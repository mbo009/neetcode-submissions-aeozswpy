class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = 0
        j = len(nums) - 1
        curr_min = float('inf')
        while i < j:
            if nums[i] > nums[j]:
                i += 1
            else:
                j -= 1
            curr_min = min(nums[i], nums[j])

        return curr_min
