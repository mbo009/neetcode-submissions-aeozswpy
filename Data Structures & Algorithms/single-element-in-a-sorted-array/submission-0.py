class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            is_left_same = (m > 0 and nums[m] == nums[m-1])
            is_right_same = (m < len(nums) - 1 and nums[m] == nums[m+1])
            
            if not is_left_same and not is_right_same:
                return nums[m]

            if is_left_same:
                if (m - 1) % 2 == 0:
                    l = m + 1
                else:
                    r = m - 2

            elif is_right_same:
                if m % 2 == 0:
                    l = m + 2
                else:
                    r = m - 1

        return -1