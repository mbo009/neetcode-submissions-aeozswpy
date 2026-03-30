class Solution:
    def rob(self, nums: List[int]) -> int:   
        if len(nums) <= 2:
            return max(nums)
    

        def rob_dp(nums):
            if len(nums) <= 2:
                return max(nums)

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[0] + nums[2]

            for i in range(3, len(nums)):
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            
            return max(dp[len(nums) - 1], dp[len(nums) - 2])
        
        return max(rob_dp(nums[1:]), rob_dp(nums[:-1]))
