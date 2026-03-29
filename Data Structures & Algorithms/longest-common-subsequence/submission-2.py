from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(None)
        def common_sub(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            curr_max = 0
            if text1[i] != text2[j]:
                curr_max = max(curr_max, common_sub(i, j + 1), common_sub(i + 1, j))
            
            if text1[i] == text2[j]:
                curr_max = 1 + max(curr_max, common_sub(i + 1, j + 1))
            
            return curr_max
        
        return common_sub(0, 0)