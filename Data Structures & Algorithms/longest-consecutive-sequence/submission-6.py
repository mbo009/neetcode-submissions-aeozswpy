class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        
        starts = sorted([num for num in nums_set if num - 1 not in nums_set])
        ends = sorted([num for num in nums_set if num + 1 not in nums_set])

        max_len = 0
        for start, end in zip(starts, ends):
            max_len = max(max_len, end - start + 1)
            
        return max_len