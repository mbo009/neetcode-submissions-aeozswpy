from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list)

        for i, num in enumerate(nums):
            if num in seen:
                for j in seen[num]:
                    if abs(i - j) <= k:
                        return True

            seen[num].append(i)
            
        return False