class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        mid = len(nums) // 2
        high = len(nums) - 1
        last_mid = -1

        while mid != last_mid:
            last_mid = mid
            if nums[low] == target:
                return low
            if nums[mid] == target:
                return mid
            if nums[high] == target:
                return high
            elif nums[mid] < target:
                low = mid
                mid += (high - mid) // 2
            else:
                high = mid
                mid -= (mid - low) // 2

        return -1