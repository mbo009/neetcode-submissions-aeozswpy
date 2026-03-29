class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combinationRec(i, curr_sum, curr_path):
            if curr_sum == target:
                res.append(curr_path[:])
                return

            if i >= len(nums) or curr_sum > target:
                return
            
            curr_path.append(nums[i])
            combinationRec(i, curr_sum + nums[i], curr_path)
            del curr_path[-1]
            combinationRec(i + 1, curr_sum, curr_path)
        
        combinationRec(0, 0, [])
        return res