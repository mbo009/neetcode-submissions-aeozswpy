class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0 : 1}
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        
        return res

# [2, -1, 1, 2]
# prefix = [0, 2, 1, 2, 4]
# sufix =  [0, 2, 3, 2, 4]

# if prefix - suffix == 0