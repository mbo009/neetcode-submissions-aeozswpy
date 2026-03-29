class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        candidate = strs[0]
        curr_max = len(candidate)

        for word in strs[1:]:
            j = 0
            while j < min(curr_max, len(word)) and candidate[j] == word[j]:
                j += 1
        
            curr_max = j
        
        return candidate[0:curr_max]

