from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        unique = list(count.keys())
    
        def subsets_rec(i, curr_path):
            if i == len(unique):
                res.append(curr_path[:])
                return
            
            if count[unique[i]] > 0:
                curr_path.append(unique[i])
                count[unique[i]] -= 1
                subsets_rec(i, curr_path)

                count[unique[i]] += 1
                del curr_path[-1]
        
            subsets_rec(i + 1, curr_path)
    
        subsets_rec(0, [])
        return res
