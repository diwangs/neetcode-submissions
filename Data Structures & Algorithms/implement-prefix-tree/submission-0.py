class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root
        for char in word:
            if not char in n.children:
                n.children[char] = TrieNode()
            n = n.children[char]
        n.eow = True

    def search(self, word: str) -> bool:
        n = self.root
        for char in word:
            if not char in n.children:
                return False
            n = n.children[char]
        return n.eow

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for char in prefix:
            if not char in n.children:
                return False
            n = n.children[char]
        return True
        