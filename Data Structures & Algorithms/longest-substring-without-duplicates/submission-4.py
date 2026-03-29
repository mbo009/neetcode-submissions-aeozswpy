class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_dict = {}
        i = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in curr_dict and curr_dict[s[j]] >= i:
                i = curr_dict[s[j]] + 1
            
            curr_dict[s[j]] = j
            max_len = max(max_len, j - i + 1)
        
        return max_len