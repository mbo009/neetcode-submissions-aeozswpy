import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (dist, [x, y]))
            else:
                if dist > heap[0][0]:
                    heapq.heapreplace(heap, (dist, [x, y]))
        
        return [p for d, p in heap]
# Brute force: iterate through points and calculate the distance to 0,0.
# Sort the points based on the distance
# return first k elements

# Optimal solution: use min stack, where first element is currently the biggest one from k vistied.
# after len(stack) > k: if we want to add an element we have to pop one from the top.
# or we can use MinHeap for calculated values to get rid of sorting problem