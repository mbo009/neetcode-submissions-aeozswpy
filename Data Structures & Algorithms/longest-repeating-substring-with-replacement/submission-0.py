class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        max_char = 0
        max_len = 0
        i = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            max_char = max(max_char, count[s[j]])

            if j - i + 1 - max_char > k:
                count[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j - i + 1)

        return max_len
# XYYXX
# dict:
# X: 0, 3, 4
# Y: 
