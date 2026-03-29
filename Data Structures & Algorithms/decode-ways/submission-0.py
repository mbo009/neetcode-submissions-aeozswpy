class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] += dp[i + 1]

                if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and int(s[i + 1]) < 7)):
                    dp[i] += dp[i + 2]
        
        return dp[0]

# "0123"
# We can do 1 or 2 step at every idx,
# for every possible step add +1 to dp
# dp tells us how many ways of decoding there are for this step