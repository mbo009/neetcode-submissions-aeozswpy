class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_dict = {}
        max_len = 0
        i = 0

        for j in range(len(s)):
            if s[j] in index_dict and index_dict[s[j]] >= i:
                i = index_dict[s[j]] + 1
            
            index_dict[s[j]] = j
            max_len = max(max_len, j - i + 1)
        
        return max_len