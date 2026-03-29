class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)

        def kSum(k, i, target):
            if k == 1 or i >= len(nums):
                return []

            k_sums = []
            j = len(nums) - 1

            if k == 2:
                while i < j:
                    curr_sum = sorted_nums[i] + sorted_nums[j]
                    if curr_sum == target:
                        k_sums.append([sorted_nums[i], sorted_nums[j]])
                        i += 1
                        j -= 1
                        while i < j and sorted_nums[i - 1] == sorted_nums[i]:
                            i += 1
                    elif curr_sum < target:
                        i += 1
                    else:
                        j -= 1
            else:
                for m in range(i, len(nums)):
                    if m > i and sorted_nums[m] == sorted_nums[m - 1]:
                        continue 
                    sub_res = kSum(k - 1, m + 1, target - sorted_nums[m])
                
                    for subset in sub_res:
                        k_sums.append([sorted_nums[m]] + subset)
    
            return k_sums
        return kSum(4, 0, target)
