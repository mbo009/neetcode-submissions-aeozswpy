from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counter = Counter(nums)
        return [key for key, value in num_counter.items() if value > len(nums) // 3]        