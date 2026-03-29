class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_max = float('-inf')
        nums_set = set(nums)
        starts = set()

        if len(nums) == 0:
            return 0

        for num in nums:
            if num - 1 not in nums_set:
                starts.add(num)
        
        for start in starts:
            curr_len = 1
            curr_num = start + 1
            while curr_num in nums_set:
                curr_num += 1
                curr_len += 1
            
            if curr_len > curr_max:
                curr_max = curr_len
    

        return curr_max

