class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = k
        start = 0
        max_count = 0

        for i in range(len(s)):
            count[s[i]] += 1
            max_count = max(count[s[i]], max_count)

            if i - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
        
            res = max(res, i - start + 1)

        return res
