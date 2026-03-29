from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        s1_dict = Counter(s1)
        curr_dict = Counter()

        for j in range(len(s2)):
            curr_dict[s2[j]] += 1

            if j - i + 1 > len(s1):
                curr_dict[s2[i]] -= 1
                if curr_dict[s2[i]] == 0:
                    del curr_dict[s2[i]]
                i += 1
            
            if curr_dict == s1_dict:
                return True

        
        return False