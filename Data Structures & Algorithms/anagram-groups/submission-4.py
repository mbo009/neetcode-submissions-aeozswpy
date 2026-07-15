class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        group_counter = []

        for word in strs:
            word_counter = Counter(word)
            found = False

            for i, counter in enumerate(group_counter):
                if counter == word_counter:
                    grouped[i].append(word)
                    found = True
                    break

            if not found:
                group_counter.append(word_counter)
                grouped.append([word])

        return grouped
