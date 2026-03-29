from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = dict(Counter(s1))
        s2_counter = dict(Counter(s2[:len(s1)]))
        if s1_counter == s2_counter:
            return True

        for i in range(len(s1), len(s2)):
            s2_counter[s2[i - len(s1)]] -= 1
            if s2_counter[s2[i - len(s1)]] == 0:
                s2_counter.pop(s2[i - len(s1)])
            s2_counter[s2[i]] = s2_counter.get(s2[i], 0) + 1
            if s1_counter.items() == s2_counter.items():
                return True
        
        return False