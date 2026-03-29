class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set()
        i = 0
        while i < len(nums):
            print(i)
            if nums[i] in nums_set:
                del nums[i]
                i -= 1
            else:
                nums_set.add(nums[i])
            i += 1

        return len(nums)