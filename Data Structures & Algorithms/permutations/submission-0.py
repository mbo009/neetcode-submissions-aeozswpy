class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def permute_rec(i):
            if i >= len(nums):
                res.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                permute_rec(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        permute_rec(0)
        return res