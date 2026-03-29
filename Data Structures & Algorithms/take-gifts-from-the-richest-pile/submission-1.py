import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        for i in range(k):
            max_gift = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, floor(sqrt(max_gift)))
        
        return sum(gifts)