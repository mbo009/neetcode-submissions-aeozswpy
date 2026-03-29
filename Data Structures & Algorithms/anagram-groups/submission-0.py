from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = [[strs[0]]]
        anagrams_counters = [Counter(strs[0])]       
        
        for word in strs[1:]:
            is_found = False
            cur_counter = Counter(word)

            for i, counter in enumerate(anagrams_counters):
                if cur_counter == counter:
                    grouped_anagrams[i].append(word)
                    is_found = True
                    break
            
            if not is_found:
                grouped_anagrams.append([word])
                anagrams_counters.append(cur_counter)
        
        return grouped_anagrams

            

