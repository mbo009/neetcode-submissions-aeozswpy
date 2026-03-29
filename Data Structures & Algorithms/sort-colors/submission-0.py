class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for num in nums:
            buckets[num] += 1
        
        res = []
        for i, count in enumerate(buckets):
            res += [i for _ in range(count)]
        
        nums[:] = res