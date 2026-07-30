class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        starts = []
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set and num + 1 in nums_set:
                starts.append(num)
                
        longest = 1
        for start in starts:
            curr = start + 1
        
            while curr in nums_set:
                curr += 1

            longest = max(longest, curr - start)

        return longest
            