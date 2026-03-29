from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window_count = {}
        
        have = 0
        need = len(t_count)
        res = ""
        res_len = float("inf")
        i = 0

        for j in range(len(s)):
            char = s[j]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (j - i + 1) < res_len:
                    res_len = j - i + 1
                    res = s[i : j + 1]

                left_char = s[i]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                
                i += 1

        return res