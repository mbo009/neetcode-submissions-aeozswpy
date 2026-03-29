from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = (Counter(word) for word in strs)
        counters_group = []
        groups = []

        for i, counter in enumerate(counters):
            is_match = False
            for j, group in enumerate(counters_group):
                if counter.items() == group.items():
                    groups[j].append(strs[i])
                    is_match = True
                    break
                
            if not is_match:
                counters_group.append(counter)
                groups.append([strs[i]])
        
        return groups
            
                

