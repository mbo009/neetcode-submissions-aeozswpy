from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        all_words_set = set(wordList + [beginWord])
        if endWord not in all_words_set:
            return 0

        all_words = list(all_words_set)
        transformations = {word: [] for word in all_words}

        for i in range(len(all_words)):
            for j in range(i + 1, len(all_words)):
                w1, w2 = all_words[i], all_words[j]
                
                diff = 0
                for k in range(len(w1)):
                    if w1[k] != w2[k]:
                        diff += 1
                    if diff > 1: break
                
                if diff == 1:
                    transformations[w1].append(w2)
                    transformations[w2].append(w1)
                
    
        queue = deque([(beginWord, 1)])
        visited = set()
    
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level

            for neighbor in transformations[current_word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
                    
        return 0            



# bat, bag, sag, dag
# 
# bat - bag   -- diff: t/g
# transformations[bat] = [bag]
# transformations[bag] = [bat]

# we make a queue, we start it with words that are off by 1 compared to beginWord
# we have to make sure endWord is even possible
