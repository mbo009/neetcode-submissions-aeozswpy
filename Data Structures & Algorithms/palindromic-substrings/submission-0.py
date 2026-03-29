class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s) + 1)]
        count = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1

        return count


# Brute Force: check every possible combination if it's a palindrome then count += 1
# Better Solution: Use 2d DP where [i][j] tells us if substring from i - j is a palindrome if it is count += 1
# Optimal Solution: We lock each element as a center then expand to left and right till it's palindrome
# we can update count by difference between i and j // 2 or at every successful expand


# if j - i < 2:
# j - i == 1: aa 2 characters matching
# j - i == 0: a singular character

# if it's more than that we have to check if what's between those character is also a palindrome

