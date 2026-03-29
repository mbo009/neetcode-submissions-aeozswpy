class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_complete = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                new_node = TrieNode()
                curr.children[char] = new_node
    
            curr = curr.children[char]

        curr.is_complete = True

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            print("Search: char: ", char)
            if not char in curr.children:
                return False

            curr = curr.children[char]
        
        return curr.is_complete

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if not char in curr.children:
                return False

            curr = curr.children[char]
        
        return True

        