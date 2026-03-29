from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_counter = Counter(arr)
        max_value = -1
        for key, value in num_counter.items():
            if value == key:
                max_value = max(max_value, value)

        return max_value 