from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                right = mid - 1
            else:
                left = mid + 1
        
        start_idx = mid
        if mid + 1 < len(arr) and abs(arr[mid+1] - x) < abs(arr[mid] - x):
            start_idx = mid + 1
        if mid - 1 >= 0 and abs(arr[mid-1] - x) <= abs(arr[mid] - x):
            start_idx = mid - 1

        res = [arr[start_idx]]
        left = start_idx - 1
        right = start_idx + 1

        while len(res) < k:
            can_go_left = left >= 0
            can_go_right = right < len(arr)

            if can_go_left:
                if not can_go_right or abs(arr[left] - x) <= abs(arr[right] - x):
                    res.insert(0, arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            else:
                res.append(arr[right])
                right += 1
        
        return res