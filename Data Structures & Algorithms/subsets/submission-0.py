class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        def subsets_rec(i, curr_path):
            if i == len(nums):
                return
            
            curr_path.append(nums[i])
            res.append(curr_path[:])
            subsets_rec(i + 1, curr_path)
            del curr_path[-1]
            subsets_rec(i + 1, curr_path)
    
        subsets_rec(i, [])
        res.append([])
        return res
