class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_finished = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]

        curr.is_finished = True 

    def search(self, word: str, curr = None) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_finished

        return dfs(0, self.head)