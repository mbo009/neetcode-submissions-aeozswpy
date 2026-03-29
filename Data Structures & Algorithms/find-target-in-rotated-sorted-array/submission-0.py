class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            if abs(target - nums[i]) > abs(target - nums[j]):
                i += 1
            else:
                j -= 1
        return -1
