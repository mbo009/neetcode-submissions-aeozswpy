class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = set()

        def permute(curr):
            if len(curr) == len(nums):
                self.permutations.add(tuple(curr))
                return
            
            for i in range(len(nums)):
                if nums[i] != float('-inf'):
                    curr.append(nums[i])
                    nums[i] = float('-inf')
                    permute(curr)
                    nums[i] = curr[-1]
                    curr.pop()

        permute([])
        return list(self.permutations)
