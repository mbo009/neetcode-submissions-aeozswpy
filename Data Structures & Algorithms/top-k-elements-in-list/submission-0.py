from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common(k)
        return [element[0] for element in most_common]