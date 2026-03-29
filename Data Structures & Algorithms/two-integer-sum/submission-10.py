class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()

        if indexed_nums[0][0] + indexed_nums[1][0] > target: return []
        if indexed_nums[-1][0] + indexed_nums[-2][0] < target: return []

        i = 0
        j = len(nums) - 1

        while i < j:
            curr_sum = indexed_nums[i][0] + indexed_nums[j][0]
            if curr_sum == target:
                return sorted([indexed_nums[i][1], indexed_nums[j][1]])
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
        
        return []