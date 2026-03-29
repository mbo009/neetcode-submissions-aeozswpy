from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        c_counter = Counter(candidates)
        unique = list(c_counter.keys())
        
        def combinationRec(i, curr_sum, curr_path):
            if curr_sum == target:
                res.append(curr_path[:])
                return

            if i >= len(unique) or curr_sum > target:
                return
            
            if c_counter[unique[i]] > 0:
                c_counter[unique[i]] -= 1
                curr_path.append(unique[i])
                combinationRec(i, curr_sum + unique[i], curr_path)
                
                curr_path.pop()
                c_counter[unique[i]] += 1

            combinationRec(i + 1, curr_sum, curr_path)       
         
        combinationRec(0, 0, [])
        return res