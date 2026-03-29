class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) in (2, 3):
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = dp[0] + nums[2]

        for i in range(3, len(nums) - 1):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        
        dp_last = [0] * len(nums)
        dp_last[1] = nums[1]
        dp_last[2] = nums[2]

        for i in range(3, len(nums)):
            dp_last[i] = max(dp_last[i - 2], dp_last[i - 3]) + nums[i]
        
        max_first_pass = max(dp[len(nums) - 2], dp[len(nums) - 3])
        max_second_pass = max(dp_last[len(nums) - 1], dp_last[len(nums) - 2])
        
        return max(max_first_pass, max_second_pass)
