class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[-1]
        res = [-1]
    
        for i in range(len(arr) - 2, -1, -1):
            res.insert(0, curr_max)
            curr_max = max(arr[i], curr_max)
        
        return res