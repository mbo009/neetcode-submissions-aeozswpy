import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        i = k
        while i > 0:
            popped = heapq.heappop_max(nums)
            i -= 1
        return popped
