class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining_dict = dict()
        for i, num in enumerate(nums):
            print(remaining_dict)
            if remaining_dict.get(target - num, -1) != -1:
                return [remaining_dict[target - num], i]
            else:
                remaining_dict[num] = i

        return [-1, -1]