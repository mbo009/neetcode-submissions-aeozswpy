import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        heap = []
        for key, value in counter.items():
            heapq.heappush_max(heap, (value, key))
        
        k_frequent = []
        for _ in range(k):
            k_frequent.append(heapq.heappop_max(heap)[1])
        
        return k_frequent