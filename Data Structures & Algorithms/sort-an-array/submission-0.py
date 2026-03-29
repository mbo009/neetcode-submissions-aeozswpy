class Solution:
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
    
        mid = nums[len(nums) // 2]
        left = []
        middle = []
        right = []

        for num in nums:
            if num < mid:
                left.append(num)
            elif num > mid:
                right.append(num)
            else:
                middle.append(num)

        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums)