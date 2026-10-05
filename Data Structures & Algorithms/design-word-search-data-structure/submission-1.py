class TrieNode:
    def __init__(self):
        self.c = {}
        self.eow = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        n = self.root
        for char in word:
            if not char in n.c:
                n.c[char] = TrieNode()
            n = n.c[char]
        n.eow = True

    def search(self, word: str) -> bool:
        return search_node(self.root, word)
        
def search_node(n: TrieNode, word: str) -> bool:
    if len(word) == 0:
        return n.eow
    
    for i in range(len(word)):
        char = word[i]
        if char != ".":
            if not char in n.c:
                return False
            return search_node(n.c[char], word[i+1:])
        else:
            for child in n.c:
                if search_node(n.c[child], word[i+1:]):
                    return True
            return False

