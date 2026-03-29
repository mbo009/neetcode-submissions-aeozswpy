from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_counter = Counter(t)
        s_counter = dict()
        
        have = 0
        need = len(t_counter)
        
        min_len = float("inf")
        res = [-1, -1]
        
        i = 0

        for j in range(len(s)):
            char = s[j]
            s_counter[char] = s_counter.get(char, 0) + 1

            if char in t_counter and s_counter[char] == t_counter[char]:
                have += 1

            while have == need:
                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    res = [i, j]
                
                left_char = s[i]
                s_counter[left_char] -= 1
                
                if left_char in t_counter and s_counter[left_char] < t_counter[left_char]:
                    have -= 1
                
                i += 1
        
        l, r = res
        return s[l : r+1] if min_len != float("inf") else ""