class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combinations(i, curr_path):
            if len(curr_path) == k:
                res.append(curr_path)
                return

            if i > n:
                return
            
            combinations(i + 1, curr_path + [i])
            combinations(i + 1, curr_path)

        
        combinations(1, [])
        return res
