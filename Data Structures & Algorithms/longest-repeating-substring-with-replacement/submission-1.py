from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        i = 0
        max_len = 0
        max_count = 0

        for j in range(len(s)):
            counter[s[j]] += 1
            max_count = max(max_count, counter[s[j]])

            if (j - i + 1) - max_count > k:
                counter[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j - i + 1)
        
        return max_len